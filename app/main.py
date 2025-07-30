from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.db.database import engine
from app.db.models import Base
from app.api.v1.endpoints import auth, news
import asyncio

app = FastAPI(
    title="SimpleNews Publisher API",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
)

# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve uploaded media
app.mount("/media", StaticFiles(directory=settings.MEDIA_ROOT), name="media")

# Routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(news.router, prefix="/api/v1/news", tags=["news"])

# ✅ Async table creation at startup
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
