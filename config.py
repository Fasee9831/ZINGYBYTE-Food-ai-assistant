import logging

# 1. Platform & Version Constants
PLATFORM_NAME = "ZINGYBYTE"
VERSION = "2.0.0"

# 2. Model Configuration
DEFAULT_MODEL = "llama-3.1-8b-instant"  # Fast Groq model
AVAILABLE_MODELS = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "gemma2-9b-it", "mixtral-8x7b-32768"] 

# 3. Streamlit Page Configuration
PAGE_CONFIG = {
    "page_title": "ZingyByte AI — Smart Serve",
    "page_icon": "🍔",
    "layout": "wide"
}

# 4. Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ZingyByteApp")