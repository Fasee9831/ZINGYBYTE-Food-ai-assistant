"""Main entry orchestrator organizing execution lifecycles and application layouts."""

import re
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
)
from chat import execute_grounded_stream, update_running_summary

_IMAGE_EXT = re.compile(r'\.(jpg|jpeg|png|gif|webp|bmp|svg|ico|heic|heif|tiff?)\b', re.IGNORECASE)

def _is_image_input(text: str) -> bool:
    """Detect image data URIs or file paths the text-only model can't handle."""
    if "data:image" in text or text.strip().startswith("data:"):
        return True
    if _IMAGE_EXT.search(text):
        return True
    return False

_IMAGE_ERROR_RESPONSE = (
    "I'm a text-based food concierge and can't view images or files. "
    "Please describe what you'd like to know — menu items, prices, "
    "order status, or delivery info! 🍔"
)


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

        # Detect image/file inputs before calling the API
        is_image = _is_image_input(active_query)

        # Show a masked version for image inputs
        user_display = "[Image / File pasted]" if is_image else active_query

        st.session_state.messages.append({"role": "user", "content": user_display})
        render_chat_bubble("user", user_display)

        if is_image:
            st.session_state.messages.append({
                "role": "assistant",
                "content": _IMAGE_ERROR_RESPONSE,
            })
            render_chat_bubble("assistant", _IMAGE_ERROR_RESPONSE)
            st.rerun()
            return

        history_payload = compile_message_history()

        response_text = ""
        metrics_payload = {}
        had_error = False

        with st.chat_message("assistant"):
            text_placeholder = st.empty()
            badge_placeholder = st.empty()

            with st.spinner("🍔 Searching ZingyByte knowledge base…"):
                stream_node = execute_grounded_stream(
                    user_input=active_query,
                    history_payload=history_payload,
                    model_name=st.session_state.selected_model,
                )

                for block in stream_node:
                    if block["type"] == "token":
                        response_text += block["content"]
                        metrics_payload = block["metrics"]
                        elapsed = metrics_payload["elapsed"]
                        tokens = metrics_payload["tokens"]
                        tps = round(tokens / elapsed) if elapsed > 0 else 0

                        text_placeholder.markdown(
                            response_text + '<span class="zb-cursor"></span>',
                            unsafe_allow_html=True,
                        )
                        badge_placeholder.markdown(
                            f'<div class="zb-badge-row">'
                            f'<span class="zb-badge streaming">⏱ {elapsed:.2f}s</span>'
                            f'<span class="zb-badge streaming">🚀 {tps} t/s</span>'
                            f'<span class="zb-badge streaming">✨ Generating…</span>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )

                    elif block["type"] == "error":
                        had_error = True
                        raw = block["content"]
                        if "image" in raw.lower() or "not support" in raw.lower():
                            response_text = _IMAGE_ERROR_RESPONSE
                        else:
                            response_text = f"⚠️ {raw}"
                        text_placeholder.error(response_text)
                        break

            # Final clean render (only for success path)
            if not had_error:
                text_placeholder.markdown(response_text)
                badge_placeholder.empty()

        # Persist message to session history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response_text,
            "metrics": metrics_payload if not had_error else {},
        })

        # Side effects only on success
        if not had_error:
            update_running_summary(st.session_state.selected_model)
            if metrics_payload:
                st.session_state.metrics_history["execution_time"] = metrics_payload.get("elapsed", 0.0)

        st.rerun()


if __name__ == "__main__":
    main()
