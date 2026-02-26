from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import os
import shutil

# Apne banaye hue modules import kar rahe hain
from backend.database import get_db, UserSession
from backend.ai_engine import process_audio

app = FastAPI(
    title="AI English Tutor API", 
    description="Production-grade Backend for the AI Tutor Application",
    version="1.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome! The AI English Tutor Backend is running perfectly."}

@app.get("/health")
def health_check():
    return {"status": "100% Healthy", "ready_for_ai": True}

# 🚀 The Main Endpoint: Audio Upload & Process
@app.post("/analyze-audio")
async def analyze_audio(audio_file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    # 1. Security Check: Sirf audio files allow karo
    if not audio_file.filename.endswith(('.wav', '.mp3', '.m4a')):
        raise HTTPException(status_code=400, detail="Only .wav, .mp3, or .m4a files are allowed")
    
    # 2. File ko temporarily server par save karo
    temp_file_path = f"temp_{audio_file.filename}"
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)
        
        # 3. AI Engine (Chef) ko file bhejo
        ai_result = process_audio(temp_file_path)
        
        if ai_result["status"] == "error":
            raise HTTPException(status_code=500, detail=ai_result["feedback"])
        
        # 4. Data Pipeline: Result ko Database mein save karo
        new_session = UserSession(
            transcription=ai_result["transcription"],
            feedback=ai_result["feedback"]
        )
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        
        # 5. Final Result wapas do
        return {
            "message": "Analysis complete & saved to DB",
            "data": ai_result
        }
        
    finally:
        # 6. Memory Management: Temp file ko delete karo
        # (Production Trick: Agar AWS par file delete nahi ki, toh server full hoke crash ho jayega)
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)