

from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.user.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def create(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def remove(self, id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_user_by_username(self, username: str) -> Optional[User]:
        raise NotImplementedError
