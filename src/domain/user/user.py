from dataclasses import dataclass
from typing import List

from src.domain.debit.debit import Debit


@dataclass(init=False, eq=True, frozen=True)
class User:
    id: int
    username: str
    __password: str
    debits: List[Debit]

    @property
    def username(self):
        return self.username

    @property
    def password(self):
        return self.__password

    @property
    def debits(self):
        return self.debits
