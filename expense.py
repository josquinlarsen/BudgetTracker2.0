class Expense:

    def __init__(self, category, description, amount):
        self._category = category
        self._description = description
        self._amount = amount
       
    def __repr__(self) -> str:
        return f"<Expense: {self._description}, {self._category}, {self._amount:.2f}>"
