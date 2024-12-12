from sqlalchemy.orm import Session
from typing import TypeVar, Generic, Type

T = TypeVar("T")


class BaseCRUD(Generic[T]):
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session

    async def get_all(self):
        return await self.session.query(self.model).all()

    async def get(self, id: int):
        return await self.session.query(self.model).filter(self.model.id == id).first()

    async def create(self, obj: T):
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def update(self, id: int, obj: T):
        self.session.query(self.model).filter(self.model.id == id).update(obj.dict())
        await self.session.commit()
        return await self.get(id)

    async def delete(self, id: int):
        await self.session.query(self.model).filter(self.model.id == id).delete()
        await self.session.commit()
        return {"message": "Deleted successfully"}
