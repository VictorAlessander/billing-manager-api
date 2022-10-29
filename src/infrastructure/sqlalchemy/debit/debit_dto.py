from dependency_injector.wiring import Provide, inject
from sqlalchemy.orm import Session
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Float, Integer, String
from src.infrastructure.sqlalchemy.db import Base


class DebitDTO(Base):
    @inject
    def __init__(
        self, session: Session = Provide["Container.session"]
    ) -> None:
        self.session = session

    __tablename__ = "debits"

    id = Column(Integer, primary_key=True)
    debit_name = Column(String(100), nullable=False)
    cost = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # @classmethod
    # def find_debits_by_user(cls, user_id):
    #     def to_json(arg):
    #         return {
    #             "id": arg.id,
    #             "debit_name": arg.debit_name,
    #             "cost": arg.cost,
    #             "category_id": arg.category_id,
    #             "user_id": arg.user_id,
    #         }

    #     return {
    #         "debits": list(
    #             map(
    #                 lambda x: to_json(x),
    #                 DebitDTO.query.filter_by(user_id=user_id),
    #             )
    #         )
    #     }

    def save(self):
        self.session.add(self)
        self.session.commit()
