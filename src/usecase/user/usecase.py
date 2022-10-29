from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.user.repository import UserRepository
from src.domain.user.user import User


class UserUseCase(ABC):

    userRepository: UserRepository

    @abstractmethod
    def list_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user: User) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def remove_user(self, id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_user_by_id(self, id: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_user_by_username(self, username: str) -> Optional[User]:
        raise NotImplementedError
