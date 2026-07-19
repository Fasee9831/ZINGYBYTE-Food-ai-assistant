# 🍔 ZingyByte AI — Smart Serve

A smart food concierge chatbot that helps customers explore menus, track orders, and get food recommendations — powered by **Streamlit**, **LangChain**, and **Groq AI**.

---

## ✨ Features

- **AI Food Assistant** — Ask about menu items, prices, ratings, and customizations
- **Live Order Tracking** — Check mock order status with IDs like `ZB-9874`
- **FAQ Answers** — Get instant answers about delivery fees, policies, and payment options
- **Fast Streaming Responses** — Responses appear word-by-word in real-time
- **Premium UI** — Dark glassmorphic design with floating food animations
- **Session Stats** — Sidebar shows message count, latency, and word counts
- **Auto-Summary** — Long conversations are summarized to keep responses fast

---

## 🚀 How to Run Locally

### 1. Get the code
```bash
git clone https://github.com/YOUR_USERNAME/zingybyte-ai.git
cd zingybyte-ai
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

Create a folder and file:
```
.streamlit/secrets.toml
```

Paste this inside (get a free key at https://console.groq.com):
```toml
GROQ_API_KEY = "gsk_your_api_key_here"
```

### 4. Run the app
```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## ☁️ Deploy on Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to https://share.streamlit.io
3. Click **New app** → select your repo → set main file to `app.py`
4. Go to **Settings → Secrets** and add:
```toml
GROQ_API_KEY = "gsk_your_api_key_here"
```
5. Click **Deploy** — your app is live!

---

## 📂 Files Explained

| File | What it does |
|------|-------------|
| `app.py` | Main app — connects UI, chat logic, and streaming |
| `chat.py` | Talks to Groq AI, handles streaming and summaries |
| `config.py` | Settings — models, page config, logging |
| `knowledge.py` | Menu catalog, FAQs, and mock order data |
| `prompt.py` | AI personality instructions and suggested questions |
| `styles.py` | All the CSS for the dark premium look |
| `ui.py` | Renders sidebar, top bar, hero screen, and chat bubbles |
| `utils.py` | Session state setup, message history, and export |

---

## 💬 Try These Questions

Click the suggestion cards on the home screen or type:

> Which Broasted Chicken choices have a 5-star rating and what do they cost?

> Can you list all pizzas with prices, ratings, and customization options?

> What is the delivery fee and how do I get free delivery?

> Where is my order ZB-9874?

---

## 🛠 Tech Stack

- **Frontend**: Streamlit + custom CSS
- **AI Engine**: LangChain + Groq API
- **Models**: `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, `gemma2-9b-it`, `mixtral-8x7b-32768`

---

## 📝 License

MIT License
