from abc import ABC, abstractmethod


class RemoveBGService(ABC):
    @abstractmethod
    def apply(self, content: bytes) -> bytes:
        raise NotImplementedError
