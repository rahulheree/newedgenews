from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import async_session
from app.core.security import decode_token

oauth2_scheme = HTTPBearer()

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

async def get_current_publisher(
    credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme),
) -> str:
    token = credentials.credentials
    username = decode_token(token)
    if username != "publisher":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return username