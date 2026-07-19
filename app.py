"""Main entry orchestrator organizing execution lifecycles and application layouts."""

import streamlit as st
from config import PAGE_CONFIG

# Lock default workspace page profiles instantly before other dependencies process layouts
st.set_page_config(**PAGE_CONFIG)

from styles import inject_premium_styles
from utils import init_app_state, compile_message_history
from ui import (
    render_sidebar_controls,
    render_top_bar,
    render_empty_state_screen,
    render_active_chat_bubbles,
    render_chat_bubble,
    build_chat_bubble_html,
)
from chat import execute_grounded_stream, update_running_summary


def main() -> None:
    """Coordinates view generation loops, user inputs, and streaming engine cycles."""

    # 1. Inject the full design-system CSS
    inject_premium_styles()

    # 2. Initialise session state defaults
    init_app_state()

    # 3. Render sidebar panel
    render_sidebar_controls()

    # 4. Render top navigation bar
    render_top_bar()

    # 5. Render hero screen or live chat bubbles
    if not st.session_state.messages:
        render_empty_state_screen()
    else:
        render_active_chat_bubbles()

    # 6. Capture suggestion-card injected queries
    active_query = None
    if st.session_state.get("input_injection"):
        active_query = st.session_state.input_injection
        st.session_state.input_injection = None

    # 7. Capture manual text input
    user_text_input = st.chat_input(
        "Ask about any dish, customizations, delivery, or track your order…"
    )
    if user_text_input:
        active_query = user_text_input

    # 8. Execute query through the grounded streaming pipeline
    if active_query:

        # Reject image/file inputs — Groq text models don't support them
        if "data:image" in active_query or active_query.strip().startswith("data:"):
            st.session_state.messages.append({"role": "user", "content": "[Image/file upload detected]"})
            render_chat_bubble("user", "[Image/file upload]")
            render_chat_bubble(
                "assistant",
                "I'm a text-based food concierge and can't process images or files yet. "
                "Please describe what you'd like to know — e.g. menu items, prices, order status, or delivery info! 🍔",
            )
            return

        st.session_state.messages.append({"role": "user", "content": active_query})
        render_chat_bubble("user", active_query)

        history_payload = compile_message_history()

        streaming_placeholder = st.empty()
        streaming_placeholder.markdown(
            build_chat_bubble_html("assistant", ""),
            unsafe_allow_html=True,
        )

        accumulated_response = ""
        metrics_payload = {}

        with st.spinner("🍔 Searching ZingyByte knowledge base…"):
            stream_node = execute_grounded_stream(
                user_input=active_query,
                history_payload=history_payload,
                model_name=st.session_state.selected_model,
            )

            for block in stream_node:
                if block["type"] == "token":
                    accumulated_response += block["content"]
                    metrics_payload = block["metrics"]

                    streaming_placeholder.markdown(
                        build_chat_bubble_html(
                            "assistant",
                            accumulated_response,
                            metrics=metrics_payload,
                            show_cursor=True,
                        ),
                        unsafe_allow_html=True,
                    )

                elif block["type"] == "error":
                    error_text = block["content"]
                    # Friendlier message for image-model errors
                    if "image" in error_text.lower() or "not support" in error_text.lower():
                        friendly = (
                            "I can only process text at the moment — I can't view images or files. "
                            "Try describing what you need: menu details, order tracking, or food recommendations! 🍔"
                        )
                    else:
                        friendly = f"⚠️ {error_text}"
                    streaming_placeholder.markdown(
                        build_chat_bubble_html("assistant", friendly),
                        unsafe_allow_html=True,
                    )
                    return

        # Final clean render — remove cursor
        streaming_placeholder.markdown(
            build_chat_bubble_html("assistant", accumulated_response, metrics=metrics_payload),
            unsafe_allow_html=True,
        )

        # Persist message to session history
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": accumulated_response,
                "metrics": metrics_payload,
            }
        )

        # Update rolling conversation summary if conversation is long
        update_running_summary(st.session_state.selected_model)

        # Store last latency for sidebar display
        if metrics_payload:
            st.session_state.metrics_history["execution_time"] = metrics_payload.get(
                "elapsed", 0.0
            )

        st.rerun()


if __name__ == "__main__":
    main()
