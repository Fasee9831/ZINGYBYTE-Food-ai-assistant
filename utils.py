"""Runtime session state configuration methods and file generation handlers."""

import re
import json
from datetime import datetime
from typing import List
import streamlit as st
# Added SystemMessage to feed compiled summary to the LangChain engine
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from config import DEFAULT_MODEL, AVAILABLE_MODELS

_IMAGE_EXT_RE = re.compile(r'\.(jpg|jpeg|png|gif|webp|bmp|svg|ico|heic|heif|tiff?)\b', re.IGNORECASE)

def _redact_image_content(text: str) -> str:
    """Replace image file paths/references with a placeholder."""
    if "data:image" in text or text.strip().startswith("data:"):
        return "[Image content removed]"
    if _IMAGE_EXT_RE.search(text):
        return "[Image content removed]"
    return text

def init_app_state() -> None:
    """Safely locks standard reactive dictionary keys inside the current state context."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    else:
        # Auto-redact any stored messages containing image paths (from before the fix)
        for msg in st.session_state.messages:
            msg["content"] = _redact_image_content(msg["content"])
    if "selected_model" not in st.session_state or st.session_state.selected_model not in AVAILABLE_MODELS:
        st.session_state.selected_model = DEFAULT_MODEL
    if "metrics_history" not in st.session_state:
        st.session_state.metrics_history = {"total_tokens": 0, "execution_time": 0.0}
    if "chat_summary" not in st.session_state:
        st.session_state.chat_summary = ""

def compile_message_history() -> List:
    """Converts local state log indexes into structural message components for LangChain context mapping."""
    history = []
    
    # 1. Prepend dynamic system summary if one exists
    if st.session_state.get("chat_summary"):
        history.append(
            SystemMessage(content=f"[SUMMARY OF PRIOR CONVERSATION]: {st.session_state.chat_summary}")
        )
    
    # 2. Keep the sliding history window tiny (last 4 messages) to prevent slow inference
    active_window = st.session_state.messages[-4:]
    for msg in active_window:
        safe_content = _redact_image_content(msg["content"])
        if msg["role"] == "user":
            history.append(HumanMessage(content=safe_content))
        elif msg["role"] == "assistant":
            history.append(AIMessage(content=safe_content))
            
    return history

def export_session_logs() -> str:
    """Serializes the active session logs into a standard printable JSON layout structure."""
    return json.dumps({
        "agent": "ZingyByte AI — Smart Serve Platform",
        "timestamp": datetime.utcnow().isoformat(),
        "summary": st.session_state.get("chat_summary", ""),
        "logs": st.session_state.messages
    }, indent=2)