# Hide persistence details (SQLite, memory, file, etc.)
# Enable testing & swapping implementations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


class Repository(ABC, Generic[T]):
    """Generic repository interface for persistence abstraction."""

    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def list_all(self) -> List[T]:
        pass

    @abstractmethod
    def remove(self, entity_id: int) -> None:
        pass
