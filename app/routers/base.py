from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.backend.session import create_session
from app.const import (
    BASE_TAGS,
    BASE_URL,
)
from app.schemas.base import BaseSchema
from app.services.base import BaseService


class BaseRouter:
    def __init__(self, prefix: str, tags: list, service: BaseService):
        self.prefix = prefix
        self.tags = tags
        self.service = service
        self.router = APIRouter(prefix=self.prefix, tags=self.tags)

    async def add_route(self, path: str, endpoint: callable, methods: list = ["GET"]):
        self.router.add_api_route(path, endpoint, methods=methods)

    async def add_get_route(self, path: str, endpoint: callable):
        await self.add_route(path, endpoint, methods=["GET"])

    async def add_post_route(self, path: str, endpoint: callable):
        await self.add_route(path, endpoint, methods=["POST"])

    async def add_put_route(self, path: str, endpoint: callable):
        await self.add_route(path, endpoint, methods=["PUT"])

    async def add_delete_route(self, path: str, endpoint: callable):
        await self.add_route(path, endpoint, methods=["DELETE"])

    async def get_router(self):
        return self.router
