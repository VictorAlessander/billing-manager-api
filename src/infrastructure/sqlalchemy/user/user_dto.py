from dependency_injector.wiring import Provide, inject
from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy.orm import Session, relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from src.infrastructure.sqlalchemy.db import Base


class UserDTO(Base):
    @inject
    def __init__(
        self, session: Session = Provide["Container.session"]
    ) -> None:
        self.session = session

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    debits = relationship("DebitDTO", backref="users", lazy=True)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    # @classmethod
    # def delete_all_users(cls):
    #     try:
    #         rows_deleted = self.session.query(cls).delete()
    #         self.session.commit()

    #         return {'message': '{} rows deleted'.format(rows_deleted)}
    #     except Exception as err:
    #         print(err)
    #         return {'message': 'Something went wrong'}, 500
