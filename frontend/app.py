import streamlit as st
import requests
import os
from gtts import gTTS
import base64

# 1. Page Configuration
st.set_page_config(page_title="Aura - AI English Tutor", page_icon="🗣️", layout="wide")

# 2. Initialize Chat Memory (Session State)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 3. Custom CSS
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(to right bottom, #ffffff, #eef2f3); }
    .title-text { font-size: 3.5rem !important; font-weight: 800; background: -webkit-linear-gradient(#2E86C1, #1B4F72); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin-bottom: 0px; }
    .chat-bubble-user { background-color: #E8F8F5; padding: 15px; border-radius: 15px; margin: 10px 0; border-left: 5px solid #1ABC9C; }
    .chat-bubble-ai { background-color: #FFFFFF; padding: 15px; border-radius: 15px; margin: 10px 0; border-left: 5px solid #2E86C1; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>Aura AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5D6D7E;'>Your Personal AI Receptionist & Tutor</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # LIVE MIC
    audio_file = st.audio_input("🎙️ Speak to Aura...")
    
    if audio_file is not None:
        if st.button("✨ Analyze My English"):
            API_URL = os.getenv("API_URL", "http://backend:8000/analyze-audio")
            
            with st.spinner("🚀 Aura AI is listening..."):
                try:
                    files = {"audio_file": ("live_audio.wav", audio_file.getvalue(), "audio/wav")}
                    response = requests.post(API_URL, files=files)
                    
                    if response.status_code == 200:
                        data = response.json()["data"]
                        
                        # Save to memory
                        st.session_state.chat_history.append({"role": "user", "text": data["transcription"]})
                        st.session_state.chat_history.append({"role": "aura", "text": data["feedback"]})
                        
                        # Generate Audio (Aura's Voice)
                        tts = gTTS(text=data['feedback'], lang='en', tld='co.in') # 'co.in' gives a clear, professional accent
                        tts.save("aura_voice.mp3")
                        
                        # Autoplay Aura's voice secretly using base64 html
                        with open("aura_voice.mp3", "rb") as f:
                            audio_bytes = f.read()
                        audio_b64 = base64.b64encode(audio_bytes).decode()
                        audio_html = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}"></audio>'
                        st.markdown(audio_html, unsafe_allow_html=True)
                        
                    else:
                        st.error("Server Error!")
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown("---")
    st.markdown("### 💬 Conversation History")
    
    # Display Chat History like WhatsApp
    for chat in reversed(st.session_state.chat_history):
        if chat["role"] == "user":
            st.markdown(f"<div class='chat-bubble-user'><b>🗣️ You:</b><br><i>\"{chat['text']}\"</i></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble-ai'><b>👩‍💼 Aura:</b><br>{chat['text']}</div>", unsafe_allow_html=True)