from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    def create(self, data: dict) -> dict:
        pass

    @abstractmethod
    def get(self, id: int) -> dict:
        pass

    @abstractmethod
    def update(self, id: int, data: dict) -> dict:
        pass

    @abstractmethod
    def delete(self, id: int) -> dict:
        pass
