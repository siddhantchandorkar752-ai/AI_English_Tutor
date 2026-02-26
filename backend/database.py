from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Database ka blueprint (Schema)
Base = declarative_base()

class UserSession(Base):
    __tablename__ = 'user_sessions'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="student_01", index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    transcription = Column(String)
    feedback = Column(String)

# Local DB Engine setup
engine = create_engine('sqlite:///tutor_progress.db', connect_args={"check_same_thread": False})
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database session manage karne ka function (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()