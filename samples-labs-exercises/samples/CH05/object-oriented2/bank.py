class Account:
    def __init__(self, name: str, number: str, balance: float) -> None:
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print('存款金額不得為負')
        else:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            print('餘額不足')
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account('{self.name}', '{self.number}', {self.balance})"
