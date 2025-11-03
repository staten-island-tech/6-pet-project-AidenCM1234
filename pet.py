class Calculator():
    def add(x, y):
        print(x + y)
        return x + y

    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)

    def subtract(numbers):
        return numbers

Calculator.add(5, 6)


class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Bob =Hero("Bob", 0, ["Pencil"])
Bob.buy({"title": "Sword", "atk": 34})
print(Bob.__dict__)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

Bob =BankAccount("Bob", 10000)
Bob.show_balance()