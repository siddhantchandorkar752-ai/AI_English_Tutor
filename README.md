<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2E86C1,50:1ABC9C,100:1B4F72&height=220&section=header&text=AURA&fontSize=90&fontColor=ffffff&fontAlignY=35&desc=AI%20English%20Tutor%20%7C%20Speak%20Better%20Every%20Day&descAlignY=60&descSize=20&animation=fadeIn" width="100%"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=24&duration=3000&pause=800&color=2E86C1&center=true&vCenter=true&multiline=true&width=750&height=120&lines=🎙️+Speak+%7C+Whisper+Listens+%7C+LLaMA+Responds;Real-Time+Voice+Analysis+%2B+AI+Feedback;Whisper+%2B+LLaMA+3.1+%2B+Groq+%2B+LangChain;Your+Personal+AI+English+Coach)](https://git.io/typing-svg)

<br/>

![Python](https://img.shields.io/badge/Python-3.11-2E86C1?style=for-the-badge&logo=python&logoColor=white)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)
![LLaMA](https://img.shields.io/badge/Meta-LLaMA_3.1_8B-0064E0?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Inference-1ABC9C?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Prompt_Chain-1C3C3C?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-1B4F72?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-1ABC9C?style=for-the-badge)

<br/>

> **🎙️ Speak. Whisper listens. LLaMA teaches. Aura responds — your personal AI English coach.**

</div>

---

## 🔥 WHAT IS AURA?

```
╔══════════════════════════════════════════════════════════════════════╗
║     AURA — AI English Tutor v1.0                                    ║
║     "Not just a chatbot — a coach that listens to your voice."      ║
║                                                                      ║
║     Whisper Base  → Speech-to-Text                                  ║
║     LLaMA 3.1 8B  → Grammar Feedback + Follow-up Questions          ║
║     gTTS          → Aura speaks feedback back to you                ║
║     FastAPI + DB  → Production-grade backend with session storage   ║
╚══════════════════════════════════════════════════════════════════════╝
```

AURA is a **voice-first AI English Tutor** powered by **OpenAI Whisper** for speech recognition and **Meta LLaMA 3.1 8B** (via Groq) for intelligent grammar feedback. Speak naturally — AURA transcribes, analyzes, corrects, and **talks back to you** with personalized coaching.

---

## 😔 PROBLEM STATEMENT

Most English learning tools are:
- **Text-only** — they don't practice actual speaking
- **Passive** — scores, not real explanations
- **Expensive** — Duolingo, IELTS apps cost money
- **Not conversational** — no follow-up, no dialogue

**AURA solves this** — speak freely, get instant LLM-powered feedback with grammar correction, natural rephrasing suggestions, and a follow-up question to keep the conversation going.

---

## ⚡ CORE FEATURES

| Feature | Description | Technology |
|---------|-------------|------------|
| 🎙️ **Live Voice Input** | Speak directly into the mic in the browser | Streamlit `audio_input` |
| 📝 **Speech-to-Text** | Local Whisper Base model transcribes your speech | OpenAI Whisper |
| 🧠 **AI Grammar Feedback** | LLaMA 3.1 corrects grammar, rephrases naturally, asks follow-up | Groq + LangChain |
| 🔊 **Voice Response** | Aura's feedback converted to speech and autoplayed | gTTS (Indian accent) |
| 💬 **Chat Memory** | Full conversation history tracked across session | Streamlit Session State |
| 🗄️ **Database Storage** | Every session saved to SQLite DB (`tutor_progress.db`) | SQLAlchemy + SQLite |
| 🐳 **Docker Ready** | Frontend + Backend containerized, one command deploy | Docker Compose |

---

## 🏗️ ARCHITECTURE

```
USER SPEAKS
    │
    ▼
┌──────────────────────────────────────────────────────────┐
│                    AURA PIPELINE                         │
│                                                          │
│  ┌─────────────────────┐                                │
│  │   Streamlit UI      │ ← Live mic / audio upload      │
│  │   (Frontend :8501)  │                                │
│  └──────────┬──────────┘                                │
│             │ POST /analyze-audio                       │
│             ▼                                           │
│  ┌─────────────────────┐                                │
│  │  FastAPI Backend    │ ← File validation + routing    │
│  │  (:8000)            │                                │
│  └──────────┬──────────┘                                │
│             │                                           │
│      ┌──────▼──────────────────┐                        │
│      │      ai_engine.py       │                        │
│      │                         │                        │
│      │  Whisper Base           │ ← Audio → Text         │
│      │  LangChain Prompt       │ ← Build tutor prompt   │
│      │  Groq LLaMA 3.1 8B     │ ← Text → AI Feedback   │
│      └──────────┬──────────────┘                        │
│                 │                                        │
│      ┌──────────▼──────────────┐                        │
│      │  SQLAlchemy DB          │ ← Save session         │
│      └──────────┬──────────────┘                        │
│                 │ JSON Response                          │
│                 ▼                                        │
│  ┌─────────────────────┐                                │
│  │  gTTS Voice Engine  │ ← Feedback → MP3               │
│  │  Base64 Autoplay    │ ← Aura speaks back             │
│  └─────────────────────┘                                │
└──────────────────────────────────────────────────────────┘
```

---

## 📁 PROJECT STRUCTURE

```
AI_English_Tutor/
├── frontend/
│   ├── app.py                  ← Streamlit UI (mic, chat bubbles, autoplay)
│   └── requirements.txt
├── backend/
│   ├── __init__.py
│   ├── ai_engine.py            ← Whisper STT + LangChain + Groq LLaMA 3.1
│   ├── api.py                  ← FastAPI routes (/analyze-audio, /health)
│   └── database.py             ← SQLAlchemy models + session storage
├── Dockerfile.frontend
├── Dockerfile.backend
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── requirements.txt
```

---

## 🛠️ INSTALLATION

### Prerequisites
- Python 3.9+
- Docker + Docker Compose
- Groq API Key — free at [console.groq.com](https://console.groq.com)

### Option 1 — Docker (Recommended)

```bash
# 1. Clone
git clone https://github.com/siddhantchandorkar752-ai/AI_English_Tutor.git
cd AI_English_Tutor

# 2. Create .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# 3. Build and run
docker-compose up --build
```

- Frontend → **http://localhost:8501**
- Backend API → **http://localhost:8000**
- API Docs → **http://localhost:8000/docs**

### Option 2 — Local Setup

```bash
# Clone
git clone https://github.com/siddhantchandorkar752-ai/AI_English_Tutor.git
cd AI_English_Tutor

# Install dependencies
pip install -r requirements.txt

# Set API key
export GROQ_API_KEY=your_groq_api_key_here  # Linux/Mac
$env:GROQ_API_KEY="your_key"               # Windows PowerShell

# Start Backend
uvicorn backend.api:app --reload --port 8000

# Start Frontend (new terminal)
streamlit run frontend/app.py
```

---

## 🚀 USAGE

1. Open **http://localhost:8501**
2. Click the **🎙️ mic button** — speak in English
3. Click **"Analyze My English"**
4. AURA transcribes → analyzes → **speaks feedback back to you**
5. View full conversation history below

---

## 🧪 EXAMPLE SESSION

```
You say:    "Yesterday I goes to the market and buyed some vegetables."

Whisper:    "Yesterday I goes to the market and buyed some vegetables."

LLaMA 3.1:  • Grammar correction:
              - "goes" → "went" (past tense of 'go')
              - "buyed" → "bought" (irregular past tense)

            • Natural rephrasing:
              "Yesterday, I went to the market and bought some vegetables."

            • Follow-up question:
              "What vegetables did you buy? Were they for a special recipe?"

[Aura autoplays the feedback in Indian English accent via gTTS]
[Session saved to database]
```

---

## 🔑 API ENDPOINTS

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check — server status |
| GET | `/health` | Detailed health check |
| POST | `/analyze-audio` | Upload audio → get transcription + feedback |

**API Docs:** `http://localhost:8000/docs` (Swagger UI auto-generated by FastAPI)

---

## 🛠️ TECH STACK

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper-STT-412991?style=for-the-badge&logo=openai&logoColor=white)
![LLaMA](https://img.shields.io/badge/LLaMA_3.1_8B-0064E0?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Inference-1ABC9C?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![gTTS](https://img.shields.io/badge/gTTS-Voice-2E86C1?style=for-the-badge)

---

## 🔮 FUTURE IMPROVEMENTS

- [ ] Pronunciation scoring — phoneme level analysis
- [ ] IELTS / TOEFL specific practice modes
- [ ] Accent detection and personalized training
- [ ] Progress dashboard — track improvement over time
- [ ] Fine-tuned LLM on English teaching datasets
- [ ] Mobile app (React Native)

---

## 🤝 CONTRIBUTING

```bash
git checkout -b feature/AmazingFeature
git commit -m 'Add AmazingFeature'
git push origin feature/AmazingFeature
# Open a Pull Request
```

---

## 📄 LICENSE

Distributed under the MIT License.

---

## 👨‍💻 AUTHOR

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:2E86C1,100:1ABC9C&height=60&text=Siddhant%20Chandorkar&fontSize=28&fontColor=ffffff&fontAlign=50&fontAlignY=50" width="500"/>

<br/><br/>

[![GitHub](https://img.shields.io/badge/GitHub-siddhantchandorkar752--ai-181717?style=for-the-badge&logo=github)](https://github.com/siddhantchandorkar752-ai)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-siddhantchandorkar-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/siddhantchandorkar)

<br/>

*"I don't just build AI. I build AI that understands humans."*

</div>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1B4F72,50:1ABC9C,100:2E86C1&height=120&section=footer&text=AURA%20v1.0&fontSize=30&fontColor=ffffff&fontAlignY=65&animation=fadeIn" width="100%"/>
</div>
