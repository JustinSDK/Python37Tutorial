class Account:
    def __init__(self, name: str, number: str, balance: float) -> None:
        self.name = name
        self.number = number
        self.balance = balance

    def check_amount(self, amount: float):
        if amount <= 0:
            raise ValueError('金額必須是正數:' + str(amount))

    def deposit(self, amount: float):
        self.check_amount(amount)
        self.balance += amount

    def withdraw(self, amount: float):
        self.check_amount(amount)
        if amount > self.balance:
           raise BankingException('餘額不足')

        self.balance -= amount

    def __str__(self):
        return f"Account('{self.name}', '{self.number}', {self.balance})"

class BankingException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

