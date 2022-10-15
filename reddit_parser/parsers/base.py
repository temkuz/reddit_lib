from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def get(self): ...
