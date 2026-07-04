from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def home():
    return {
        "status": "healthy",
        "service": "PDF RAG Chatbot API"
    }