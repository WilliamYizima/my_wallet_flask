from dataclasses import dataclass
import datetime

@dataclass
class Gain:
    """dataclass for manipulate services payload"""
    description: str
    amount: float
    date: datetime

    # @property
    # def date(self) -> str:
    #     return self.date.strftime("%m/%d/%Y")

    # def __post_init__(self):
    #     """return a string for user"""
    #     self.date = self.date.strftime("%m/%d/%Y")