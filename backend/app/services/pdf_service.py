from fastapi import UploadFile
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

async def save_pdf(file:UploadFile):
    file_path= UPLOAD_DIR / file.filename

    with open(file_path,"wb") as buffer:
        buffer.write(await file.read())

    return {
        "filename":file.filename,
        "path": str(file_path)
    }