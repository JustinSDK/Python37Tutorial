class Account:
    def __init__(self, name: str, number: str, balance: float) -> None:
        self.__name = name
        self.__number = number
        self.__balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print('存款金額不得為負')
        else:
            self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            print('餘額不足')
        else:
            self.__balance -= amount

    @property
    def name(self) -> str:
        return self.__name

    @property
    def number(self) -> str:
        return self.__number

    @property
    def balance(self) -> float:
        return self.__balance

    def __str__(self):
        return f"Account('{self.__name}', '{self.__number}', {self.__balance})"

class SavingsAccount(Account):
    def __init__(self, name: str, number: str,
                       balance: float, interest_rate: float) -> None:
        super().__init__(name, number, balance)
        self.__interest_rate = interest_rate

    def __str__(self):
        acctinfo = super().__str__()
        return f'{acctinfo}\n\tInterest rate: {self.__interest_rate}'
