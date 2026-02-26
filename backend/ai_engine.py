import whisper
from langchain_groq import ChatGroq  # Naya import
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Environment variables load karna
load_dotenv()

# Speech-to-Text Model (Whisper) Load karna
print("Loading Whisper Model...")
try:
    stt_model = whisper.load_model("base") 
    print("✅ Whisper Model Loaded Successfully!")
except Exception as e:
    print(f"❌ Error loading Whisper: {e}")

# NLP Grammar & Conversation Agent Setup (Groq - Llama 3)
# Yeh automatically .env se GROQ_API_KEY utha lega
llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.2)

tutor_prompt = PromptTemplate(
    input_variables=["student_text"],
    template="""
    You are an expert English language tutor. 
    A student just said: "{student_text}"
    
    1. Correct any grammar mistakes.
    2. Suggest a more natural way to phrase it.
    3. Ask a relevant follow-up question to keep the conversation going.
    
    Format your response clearly using bullet points.
    """
)
tutor_chain = tutor_prompt | llm

def process_audio(audio_file_path: str) -> dict:
    try:
        # 1. Audio ko text mein badlo
        result = stt_model.transcribe(audio_file_path)
        student_text = result["text"]
        
        # 2. Text ko Llama 3 (Groq) ke paas bhejo feedback ke liye
        feedback = tutor_chain.invoke({"student_text": student_text})
        
        return {
            "transcription": student_text,
            "feedback": feedback.content,
            "status": "success"
        }
    except Exception as e:
        return {
            "transcription": "",
            "feedback": f"An error occurred: {str(e)}",
            "status": "error"
        }