from abc import ABC, abstractmethod
from ..config import SESSION


class BaseParser(ABC):
    @staticmethod
    def _make_request(url, params=None):
        if params is None:
            params = {}
        response = SESSION.get(url, params=params)
        response.raise_for_status()
        return response.json()

    @abstractmethod
    def get(self): ...
