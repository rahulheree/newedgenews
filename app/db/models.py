import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ARRAY
from app.db.database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    headline = Column(String(255), nullable=False)
    sub_headline = Column(String(255))
    body = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)
    tags = Column(ARRAY(String))
    media_url = Column(String)
    media_caption = Column(String)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)