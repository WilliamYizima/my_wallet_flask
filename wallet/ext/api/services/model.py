from dataclasses import dataclass


@dataclass
class Gain:
    description: str
    amount: float
    date: str

    def formatted_date(self):
        return self.date.strftime("%m/%d/%Y")

teste = Gain(description="BT",amount=50.2,date="25-11")
print(teste.amount)