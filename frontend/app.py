import streamlit as st
import requests
import os  # <-- Yeh Docker ke liye add kiya hai

# 1. Page Configuration
st.set_page_config(
    page_title="Aura - AI English Tutor",
    page_icon="🗣️",
    layout="wide" # Wide layout se content behtar spread hota hai
)

# 2. Advanced Custom CSS for Modern UI
st.markdown("""
    <style>
    /* Background and Main Font */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Premium Card Design */
    .stApp {
        background: linear-gradient(to right bottom, #ffffff, #eef2f3);
    }

    /* Title Styling with Animation */
    .title-text {
        font-size: 4rem !important;
        font-weight: 800;
        background: -webkit-linear-gradient(#2E86C1, #1B4F72);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }

    .subtitle-text {
        text-align: center;
        color: #5D6D7E;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }

    /* File Uploader Customization */
    section[data-testid="stFileUploadDropzone"] {
        border: 2px dashed #2E86C1 !important;
        background-color: #f8fbff !important;
        border-radius: 15px !important;
        padding: 2rem !important;
    }

    /* Buttons Styling */
    div.stButton > button {
        border-radius: 50px !important;
        background: linear-gradient(90deg, #2E86C1 0%, #1B4F72 100%) !important;
        color: white !important;
        font-weight: bold !important;
        padding: 0.8rem 2.5rem !important;
        border: none !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        width: auto !important;
        display: block;
        margin: 0 auto;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15) !important;
    }

    /* Result Cards */
    .result-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #2E86C1;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. UI Header Section
st.markdown("<h1 class='title-text'>Aura AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Master your English with real-time AI feedback</p>", unsafe_allow_html=True)

# Layout Columns for better spacing
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("### 🎙️ Let's get started")
    audio_file = st.file_uploader("Upload your recording", type=['wav', 'mp3', 'm4a'], label_visibility="collapsed")
    
    if audio_file is not None:
        st.info("✅ Audio Uploaded Successfully!")
        st.audio(audio_file)
        
        analyze_btn = st.button("✨ Start Analysis")
        
        if analyze_btn:
            # DOCKER READY API URL: Yeh automatically detect karega ki Docker me hai ya local
            API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/analyze-audio")
            
            with st.spinner("🚀 Aura AI is processing your voice..."):
                try:
                    files = {"audio_file": (audio_file.name, audio_file.getvalue(), audio_file.type)}
                    response = requests.post(API_URL, files=files)
                    
                    if response.status_code == 200:
                        result = response.json()
                        data = result["data"]
                        
                        st.balloons()
                        st.success("Analysis Complete!")
                        
                        # Results Section with Better Visuals
                        st.markdown("---")
                        
                        # Transcription Card
                        st.markdown("""
                            <div class='result-card'>
                                <h4 style='color: #2E86C1; margin-top: 0;'>📝 Transcription</h4>
                                <p style='font-style: italic; color: #34495E;'>"{}"</p>
                            </div>
                        """.format(data['transcription']), unsafe_allow_html=True)

                        # Feedback Card
                        st.markdown("""
                            <div class='result-card' style='border-left-color: #27AE60;'>
                                <h4 style='color: #27AE60; margin-top: 0;'>👨‍🏫 AI Feedback</h4>
                                <p style='color: #34495E;'>{}</p>
                            </div>
                        """.format(data['feedback']), unsafe_allow_html=True)
                        
                    else:
                        st.error(f"Server Error: {response.text}")
                        
                except requests.exceptions.ConnectionError:
                    st.error("🚨 Backend se connect nahi ho pa raha. Pehle FastAPI server start karein!")
                except Exception as e:
                    st.error(f"Error: {e}")

# Sidebar for additional info
with st.sidebar:
    st.title("About Aura")
    st.write("Aura uses advanced speech-to-text and LLM models to help you speak better English.")
    st.divider()
    st.caption("v1.0.0 | Powered by Groq & Streamlit")