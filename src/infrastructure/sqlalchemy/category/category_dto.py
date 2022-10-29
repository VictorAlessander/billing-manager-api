from dependency_injector.wiring import Provide, inject
from sqlalchemy.orm import Session, relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from src.infrastructure.sqlalchemy.db import Base


class Category(Base):
    @inject
    def __init__(
        self, session: Session = Provide["Container.session"]
    ) -> None:
        self.session = session

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    debits = relationship("DebitDTO", backref="category", lazy=True)

    def save(self):
        self.session.add(self)
        self.session.commit()

    # @classmethod
    # def return_all_categories(cls):
    #     def to_json(arg):
    #         return {"id": arg.id, "name": arg.name}

    #     return {
    #         "categories": list(
    #             map(lambda x: to_json(x), self.session.query().all())
    #         )
    #     }
