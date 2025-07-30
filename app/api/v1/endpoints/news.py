from typing import List, Optional
from fastapi import APIRouter, Depends, File, Form, UploadFile, HTTPException   
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.dependencies import get_db, get_current_publisher
from app.crud.news import news as crud_news
from app.schemas.news import NewsCreate, NewsUpdate, NewsOut
from app.services.media_processing import save_and_optimize

router = APIRouter()

@router.post("/", response_model=NewsOut)
async def create_news(
    headline: str = Form(...),
    sub_headline: str = Form(None),
    body: str = Form(...),
    category: str = Form(...),
    tags: str = Form(None),
    media_caption: str = Form(None),
    media: Optional[UploadFile] = File(None),
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_current_publisher),
):
    tag_list = tags.split(",") if tags else None
    obj_in = NewsCreate(
        headline=headline,
        sub_headline=sub_headline,
        body=body,
        category=category,
        tags=tag_list,
        media_caption=media_caption,
    )
    media_url = await save_and_optimize(media) if media else None
    return await crud_news.create(db, obj_in=obj_in, media_url=media_url)

@router.get("/", response_model=List[NewsOut])
async def list_news(
    category: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return await crud_news.get_multi(db, category=category, skip=skip, limit=limit)

@router.get("/{id}", response_model=NewsOut)
async def get_news(id: int, db: AsyncSession = Depends(get_db)):
    item = await crud_news.get(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Article not found")
    return item

@router.put("/{id}", response_model=NewsOut)
async def update_news(
    id: int,
    obj_in: NewsUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_current_publisher),
):
    item = await crud_news.get(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Article not found")
    return await crud_news.update(db, db_obj=item, obj_in=obj_in)

@router.delete("/{id}", response_model=NewsOut)
async def delete_news(
    id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_current_publisher),
):
    item = await crud_news.get(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Article not found")
    await crud_news.delete(db, id=id)
    return item