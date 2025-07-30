import os
import uuid
from PIL import Image
from fastapi import UploadFile
from app.core.config import settings

os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

async def save_and_optimize(file: UploadFile) -> str:
    ext = file.filename.split(".")[-1].lower()
    filename = f"{uuid.uuid4().hex}.{ext}"
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    if ext in {"jpg", "jpeg", "png", "webp"}:
        with Image.open(file_path) as img:
            img.thumbnail((1280, 720))
            img.save(file_path, optimize=True, quality=85)
    return f"/media/{filename}"