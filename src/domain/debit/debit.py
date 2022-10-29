

from dataclasses import dataclass

from src.domain.category.category import Category


@dataclass(init=False, eq=True, frozen=True)
class Debit:
    id: int
    name: str
    __cost: float
    category: Category

    def __init__(self) -> None:
        pass

    @property
    def category(self):
        return self.category

    @property
    def cost(self):
        return self.__cost
