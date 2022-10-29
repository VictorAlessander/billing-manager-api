
from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class Category:
    id: int
    name: str

    def __init__(self) -> None:
        pass

    @property
    def name(self):
        return self.name
