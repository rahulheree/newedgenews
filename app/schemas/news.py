from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class NewsCreate(BaseModel):
    headline: str = Field(..., max_length=255)
    sub_headline: Optional[str] = None
    body: str
    category: str
    tags: Optional[List[str]] = None
    media_caption: Optional[str] = None

class NewsUpdate(BaseModel):
    headline: Optional[str] = None
    sub_headline: Optional[str] = None
    body: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    media_caption: Optional[str] = None

class NewsOut(NewsCreate):
    id: int
    media_url: Optional[str] = None
    published_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True