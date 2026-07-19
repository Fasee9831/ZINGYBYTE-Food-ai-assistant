# 🍔 ZingyByte AI — Smart Serve

**ZingyByte AI** is a lightning-fast, full-stack virtual food concierge built with **Streamlit**, **LangChain**, and the **Groq API**. It serves as a smart restaurant assistant that helps customers explore the menu, track orders, get food recommendations, and find answers to FAQs—all through a beautiful, responsive, and animated chat interface.

---

## ✨ Features

- **Blazing Fast AI Responses:** Powered by `llama3-8b-8192` via the Groq API for near-instant token streaming.
- **Context-Grounded Knowledge Base:** The AI is strictly grounded using a custom knowledge dictionary, ensuring it only recommends actual menu items, real prices, and accurate store policies.
- **Live Order Tracking:** Customers can type in mock order numbers (e.g., `ZB-9874`) to get simulated real-time delivery tracking and ETA updates.
- **Beautiful Premium UI:** Custom CSS injections provide a modern, sleek interface with floating animations, dynamic metric badges, and interactive suggestion cards.
- **Session Analytics:** A sidebar tracks your conversation stats, including real-time generation speed (tokens per second), total words, and latency metrics.
- **Dynamic Memory Summarization:** Automatically summarizes older parts of the conversation to keep the context window small and inference speeds high.

---

## 🛠️ Tech Stack

- **Frontend / UI:** [Streamlit](https://streamlit.io/) (with heavy custom CSS styling)
- **Orchestration:** [LangChain](https://www.langchain.com/)
- **LLM Engine:** [Groq Cloud](https://groq.com/) (`langchain-groq`)

---

## 🚀 Quick Start (Local Execution)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/zingybyte-ai.git
cd zingybyte-ai
```

### 2. Install Dependencies
Ensure you have Python 3.9+ installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Setup your Groq API Key
1. Create a `.streamlit` folder in the root directory.
2. Inside that folder, create a `secrets.toml` file.
3. Add your Groq API key (get one free at [console.groq.com](https://console.groq.com/)):
```toml
# .streamlit/secrets.toml
GROQ_API_KEY = "gsk_your_api_key_here..."
```

### 4. Run the Application
```bash
streamlit run app.py
```
Your app will automatically open in your default browser at `http://localhost:8501`.

---

## ☁️ Deployment (Streamlit Community Cloud)

This app is optimized for seamless deployment on Streamlit Community Cloud:
1. Push this repository to your GitHub account.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and click **New app**.
3. Select this repository and set the main file path to `app.py`.
4. Click **Advanced settings** (or go to App Settings -> Secrets after deploying) and paste your API key in the Secrets block:
```toml
GROQ_API_KEY = "gsk_your_api_key_here..."
```
5. Click **Deploy!**

---

## 📂 Project Structure

- `app.py`: The main orchestrator connecting views, state, and the LLM engine.
- `chat.py`: LangChain execution logic, stream handling, and memory summarization.
- `config.py`: Global constants, UI text configs, and active model settings.
- `knowledge.py`: The data layer containing the menu catalog, FAQs, and mock order statuses.
- `prompt.py`: The system instructions defining ZingyByte's personality and rules.
- `styles.py`: Massive CSS definitions powering the premium aesthetic.
- `ui.py`: Renders sidebars, top bars, hero screens, and dynamic metric badges.
- `utils.py`: Helpers for session state initialization and log exporting.

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
