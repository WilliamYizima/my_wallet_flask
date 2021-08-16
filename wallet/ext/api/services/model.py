from dataclasses import dataclass
import datetime

@dataclass
class Gain:
    """dataclass for manipulate services payload"""
    description: str
    amount: float
    date: datetime = datetime.datetime.utcnow()

    def __post_init__(self):
        self.date = self.date.strftime("%m/%d/%Y")