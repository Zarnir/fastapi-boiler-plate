from fastapi import Depends
from sqlalchemy.orm import Session

from app.backend.session import create_session
from app.services.base import BaseService


class BaseController:
    def __init__(self, service: BaseService):
        self.service = service

    def get_db(self):
        return Depends(create_session)

    def get_service(self):
        return self.service
