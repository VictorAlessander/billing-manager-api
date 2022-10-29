from typing import List, Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from src.domain.user.repository import UserRepository
from src.domain.user.user import User


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session, user_class) -> None:
        self.session = session
        self.user = user_class

    def get_users(self) -> List[User]:
        def to_json(arg):
            return {
                "id": arg.id,
                "username": arg.username,
                "password": arg.password,
            }

        return {
            "users": list(
                map(lambda x: to_json(x), self.session.query(self.user).all())
            )
        }

    def save_user(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()

    def remove(self, id: int) -> None:
        self.session.query(self.user).filter_by(id=id).delete()
        self.session.commit()

    def find_by_id(self, id: int) -> Optional[User]:
        try:
            return self.session.query(self.user).filter_by(id=id).one()
        except NoResultFound:
            return None

    def find_user_by_username(self, username: str) -> Optional[User]:
        return (
            self.session.query(self.user).filter_by(username=username).first()
        )

    def create(self, user: User) -> None:
        return super().create(user)

    def update(self, user: User) -> User:
        return super().update(user)
