"""Renders layout views, sidebar controls, top bar, and chat bubbles."""

from datetime import datetime
import streamlit as st
from config import PLATFORM_NAME
from prompt import SUGGESTED_PROMPTS
from utils import (
    save_current_conversation, load_conversation,
    start_new_conversation, get_conversation_groups, search_conversations,
    rename_conversation, generate_pdf_export,
    Conversation
)


def _divider() -> None:
    st.markdown("<hr>", unsafe_allow_html=True)


def render_sidebar_controls() -> None:
    if "ui_font_size" not in st.session_state:
        st.session_state.ui_font_size = 15

    with st.sidebar:
        # ── Brand Block ──────────────────────────────────
        st.markdown(
            f"""
            <div class="zb-sidebar-brand">
                <div class="zb-logo-row">
                    <div class="zb-logo-icon">&#127828;</div>
                    <div class="zb-logo-text">
                        <strong>{PLATFORM_NAME} AI</strong>
                        <span>Your Food Buddy</span>
                    </div>
                </div>
                <span class="zb-status-pill">I'm here! 🍔</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        _divider()

        # ── Conversation History ──────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#128195; Conversations</p>",
            unsafe_allow_html=True,
        )

        # Search input
        search_query = st.text_input(
            "Search conversations",
            value=st.session_state.get("search_query", ""),
            placeholder="🔍 Find a chat...",
            label_visibility="collapsed",
            key="conv_search_input",
        )
        if search_query != st.session_state.get("search_query", ""):
            st.session_state.search_query = search_query
            st.rerun()

        if search_query:
            results = search_conversations(search_query)
            if results:
                for conv_id, conv in results:
                    _render_conversation_item(conv_id, conv)
            else:
                st.markdown("<div class='zb-no-convs'>No chats found</div>", unsafe_allow_html=True)
        else:
            groups = get_conversation_groups()
            has_any = False
            for group_name in ["Today", "Yesterday", "Previous 7 Days", "Older"]:
                items = groups[group_name]
                if items:
                    has_any = True
                    st.markdown(f"<span class='zb-conv-group-label'>{group_name}</span>", unsafe_allow_html=True)
                    for conv_id, conv in items:
                        _render_conversation_item(conv_id, conv)
            if not has_any:
                st.markdown("<div class='zb-no-convs'>No chats yet — ask me something!</div>", unsafe_allow_html=True)

        _divider()

        # ── Interface Scale ──────────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#127912; Text Scale</p>",
            unsafe_allow_html=True,
        )
        st.session_state.ui_font_size = st.slider(
            "Text size (px)",
            min_value=12,
            max_value=20,
            value=st.session_state.ui_font_size,
            step=1,
            help="Adjust global text size for readability.",
            label_visibility="collapsed",
        )

        _divider()

        # ── Actions ──────────────────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#9881;&#65039; Actions</p>",
            unsafe_allow_html=True,
        )
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("&#x1F4C4; New Chat", use_container_width=True, help="Save current chat and start fresh"):
                start_new_conversation()
                st.rerun()
        with col_b:
            pdf_bytes = generate_pdf_export()
            if pdf_bytes is not None:
                st.download_button(
                    label="&#x1F4D5; Download Chat as PDF",
                    data=pdf_bytes,
                    file_name="zingybyte_chat.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    help="Save this conversation as a PDF",
                )
            else:
                st.button(
                    "&#x1F4D5; Download Chat as PDF",
                    disabled=True,
                    use_container_width=True,
                    help="Install fpdf2 to enable PDF export",
                )

        _divider()

        # ── Quick Tips ───────────────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#128161; Quick Tips</p>",
            unsafe_allow_html=True,
        )
        tips = [
            ("&#127831;", "Ask me about any dish — I'll share the price and rating!"),
            ("&#128661;", "Share your <b>ZB-XXXX</b> code to track an order"),
            ("&#10024;", "Ask for <b>combo deals</b> to save more!"),
            ("&#128172;", "Curious about <b>delivery fees</b> or cancellations?"),
        ]
        tip_html = '<div class="zb-tips">'
        for icon, text in tips:
            tip_html += (
                f'<div class="zb-tip-row">'
                f'<span class="zb-tip-icon">{icon}</span>'
                f'<span>{text}</span>'
                f'</div>'
            )
        tip_html += '</div>'
        st.markdown(tip_html, unsafe_allow_html=True)

        # Keyboard shortcut hint
        st.markdown(
            '<div class="zb-kbd-hint">'
            '<kbd>Ctrl</kbd>+<kbd>K</kbd> Jump to chat &middot; '
            '<kbd>Esc</kbd> Clear search'
            '</div>',
            unsafe_allow_html=True
        )


def _render_conversation_item(conv_id: str, conv: Conversation) -> None:
    is_active = conv_id == st.session_state.current_conv_id
    active_cls = " active" if is_active else ""

    # Time ago display
    delta = datetime.now() - conv.updated_at
    if delta.total_seconds() < 60:
        time_ago = "just now"
    elif delta.total_seconds() < 3600:
        time_ago = f"{int(delta.total_seconds() // 60)}m ago"
    elif delta.total_seconds() < 86400:
        time_ago = f"{int(delta.total_seconds() // 3600)}h ago"
    else:
        time_ago = f"{int(delta.total_seconds() // 86400)}d ago"

    # Rename mode
    is_renaming = st.session_state.get("renaming_conv") == conv_id

    st.markdown(
        f"""
        <div class="zb-conv-item{active_cls}">
            <span class="zb-conv-title-text">{conv.title}</span>
            <div class="zb-conv-meta">
                <span>{time_ago}</span>
                <span>{conv.message_count} messages</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Conversation action buttons
    cols = st.columns([1, 1, 1, 2])
    with cols[0]:
        if st.button("▶", key=f"load_{conv_id}", help="Load conversation"):
            save_current_conversation()
            load_conversation(conv_id)
            st.rerun()
    with cols[1]:
        if st.button("✎", key=f"rename_{conv_id}", help="Rename"):
            st.session_state.renaming_conv = conv_id
            st.rerun()
    with cols[2]:
        if st.button("✕", key=f"delete_{conv_id}", help="Delete"):
            if conv_id in st.session_state.conversations:
                del st.session_state.conversations[conv_id]
                if conv_id == st.session_state.current_conv_id:
                    start_new_conversation()
                st.rerun()

    # Rename input
    if is_renaming:
        new_title = st.text_input(
            "Rename",
            value=conv.title,
            key=f"rename_input_{conv_id}",
            label_visibility="collapsed",
        )
        save_col, cancel_col = st.columns([1, 1])
        with save_col:
            if st.button("Save", key=f"rename_save_{conv_id}"):
                rename_conversation(conv_id, new_title)
                st.session_state.renaming_conv = None
                st.rerun()
        with cancel_col:
            if st.button("Cancel", key=f"rename_cancel_{conv_id}"):
                st.session_state.renaming_conv = None
                st.rerun()


# ──────────────────────────────────────────────────────────
# TOP NAVIGATION BAR
# ──────────────────────────────────────────────────────────

def render_top_bar() -> None:
    msgs    = st.session_state.get("messages", [])
    turns   = sum(1 for m in msgs if m["role"] == "user")
    turn_label = f"{turns} turn" if turns == 1 else f"{turns} turns"

    html_str = f"""
<div class="zb-topbar">
    <div class="zb-topbar-left">
        <span class="zb-topbar-icon">&#127828;</span>
        <span class="zb-topbar-name">ZingyByte AI</span>
        <span class="zb-topbar-sep">/</span>
        <span class="zb-topbar-sub">Your Food Guide</span>
    </div>
    <div class="zb-topbar-right">
        <span class="zb-chip">&#128172; {turn_label}</span>
    </div>
</div>
"""
    st.markdown(html_str, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# WELCOME SECTION
# ──────────────────────────────────────────────────────────

def render_welcome_section() -> None:
    st.markdown(
        """
        <div class="zb-welcome">
            <div class="zb-welcome-title">👋 Hi, Welcome to ZingyByte!</div>
            <div class="zb-welcome-sub">I'm your personal AI Food Assistant.</div>
            <div class="zb-welcome-items">
                <span class="zb-welcome-item">🍔 Find delicious meals</span>
                <span class="zb-welcome-item">🍕 Recommend dishes</span>
                <span class="zb-welcome-item">⭐ Discover top-rated food</span>
                <span class="zb-welcome-item">🛵 Track your orders</span>
                <span class="zb-welcome-item">💳 Delivery &amp; payment support</span>
            </div>
            <div class="zb-welcome-tagline">✨ What would you like to eat today?</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────────────────
# EMPTY STATE / HERO
# ──────────────────────────────────────────────────────────

def render_empty_state_screen() -> None:
    food_emojis = ["🍔", "🍟", "🍕", "🌭", "🍿", "🍩", "🍗", "🌮", "🥪", "🥤", "🍦", "🥓"]
    food_html = '<div class="zb-food-bg">'
    for emoji in food_emojis:
        food_html += f'<div class="zb-food-item">{emoji}</div>'
    food_html += '</div>'
    st.markdown(food_html, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="zb-hero">
            <span class="zb-hero-icon">&#127828;</span>
            <h1 class="zb-hero-title">ZingyByte AI</h1>
            <p class="zb-hero-sub">Your food buddy &mdash; menus, orders &amp; deals in seconds.</p>
            <div class="zb-hero-badge-wrap">
                <span class="zb-hero-badge">Always up to date with our latest menu!</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_welcome_section()

    st.markdown(
        "<p class='zb-grid-label'>Try asking me...</p>",
        unsafe_allow_html=True,
    )

    cols = st.columns(2, gap="medium")
    for idx, card in enumerate(SUGGESTED_PROMPTS):
        parts = card["label"].split(" ", 1)
        emoji = parts[0] if parts else "&#127374;"
        title = parts[1] if len(parts) > 1 else card["label"]
        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="zb-card">
                    <span class="zb-card-emoji">{emoji}</span>
                    <span class="zb-card-title">{title}</span>
                    <span class="zb-card-desc">{card['query']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Ask this", key=f"preset_{idx}", use_container_width=True):
                st.session_state.input_injection = card["query"]
                st.rerun()


# ──────────────────────────────────────────────────────────
# CHAT BUBBLE RENDERER
# ──────────────────────────────────────────────────────────

def render_chat_bubble(role: str, content: str) -> None:
    with st.chat_message(role):
        st.markdown(content)
        if role == "assistant":
            escaped = content.replace("`", "\\`").replace("'", "\\'").replace("\n", "\\n")
            action_html = (
                '<div class="zb-chat-actions">'
                '<button class="zb-chat-action-btn" onclick="'
                "var btn=this; navigator.clipboard.writeText('" + escaped + "').then(function(){ "
                "btn.classList.add('copied'); btn.textContent='\u2713 Copied'; "
                "setTimeout(function(){ btn.classList.remove('copied'); btn.textContent='\U0001f4cb Copy'; }, 2000); "
                "})"
                '">\U0001f4cb Copy</button>'
                '</div>'
            )
            st.markdown(action_html, unsafe_allow_html=True)


def render_followup_questions(suggestions: list) -> None:
    if not suggestions:
        return
    st.markdown(
        '<div class="zb-followup-section"><span class="zb-followup-label">\U0001f4a1 Try asking</span></div>',
        unsafe_allow_html=True,
    )
    cols = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(suggestion, key=f"fu_{i}", use_container_width=True):
                st.session_state.input_injection = suggestion
                st.rerun()


def render_active_chat_bubbles() -> None:
    for message in st.session_state.messages:
        render_chat_bubble(message["role"], message["content"])

    # Render follow-up questions after the last assistant message
    if st.session_state.messages:
        last_msg = st.session_state.messages[-1]
        if last_msg["role"] == "assistant":
            last_content = last_msg["content"]
            # Find last user message
            last_user = ""
            for msg in reversed(st.session_state.messages):
                if msg["role"] == "user":
                    last_user = msg["content"]
                    break
            from prompt import generate_followup_suggestions
            suggestions = generate_followup_suggestions(last_user, last_content)
            render_followup_questions(suggestions)
