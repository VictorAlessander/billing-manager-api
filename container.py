from dependency_injector import containers, providers
from sqlalchemy.orm import Session

from src.infrastructure.sqlalchemy.user.repository import UserRepositoryImpl
from src.infrastructure.sqlalchemy.user.user_dto import UserDTO
from src.usecase.user.usecaseimpl import UserUseCaseImpl


class Container(containers.DeclarativeContainer):
    session = providers.Dependency(Session)

    repository = providers.Singleton(
        UserRepositoryImpl, session=session, user_class=UserDTO
    )

    service = providers.Factory(UserUseCaseImpl, repository=repository)
