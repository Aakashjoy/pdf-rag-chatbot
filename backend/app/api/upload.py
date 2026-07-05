from fastapi import APIRouter,File,UploadFile
from ..services.pdf_service import save_pdf
router = APIRouter()

@router.post("/upload")
async def upload(file:UploadFile = File(...)):
    result =await save_pdf(file)
    return result

