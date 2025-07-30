from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from fastapi import HTTPException  # ← add this
from app.db.models import Article
from app.schemas.news import NewsCreate, NewsUpdate
from typing import List, Optional


class CRUDNews:
    async def create(
        self, db: AsyncSession, *, obj_in: NewsCreate, media_url: Optional[str] = None
    ) -> Article:
        db_obj = Article(**obj_in.model_dump(), media_url=media_url)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_multi(
        self, db: AsyncSession, *, category: Optional[str] = None, skip=0, limit=100
    ) -> List[Article]:
        stmt = select(Article).order_by(desc(Article.published_at))
        if category:
            stmt = stmt.where(Article.category == category)
        stmt = stmt.offset(skip).limit(limit)
        res = await db.execute(stmt)
        return list(res.scalars().all())

    async def get(self, db: AsyncSession, id: int) -> Optional[Article]:
        res = await db.execute(select(Article).where(Article.id == id))
        return res.scalar_one_or_none()

    async def update(
        self, db: AsyncSession, *, db_obj: Article, obj_in: NewsUpdate
    ) -> Article:
        update_data = obj_in.model_dump(exclude_unset=True)
        for k, v in update_data.items():
            setattr(db_obj, k, v)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, *, id: int) -> Article:
        obj = await self.get(db, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Article not found")
        await db.delete(obj)
        await db.commit()
        return obj


news = CRUDNews()