from typing import List, Optional

from dependency_injector.wiring import Provide, inject
from src.domain.user.repository import UserRepository
from src.domain.user.user import User
from src.usecase.user.usecase import UserUseCase


class UserUseCaseImpl(UserUseCase):
    @inject
    def __init__(
        self, repository: UserRepository = Provide["Container.repository"]
    ) -> None:
        self.repository = repository

    def list_users(self) -> List[User]:
        return self.repository.get_users()

    def find_user_by_username(self, username: str) -> Optional[User]:
        return self.repository.find_user_by_username(username)

    def create_user(self, user: User) -> None:
        return super().create_user(user)

    def find_user_by_id(self, id: int) -> Optional[User]:
        return super().find_user_by_id(id)

    def update_user(self, user: User) -> Optional[User]:
        return super().update_user(user)

    def remove_user(self, id: int) -> None:
        return super().remove_user(id)
