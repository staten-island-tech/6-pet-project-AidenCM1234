"""class Calculator():
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
Bob.show_balance()"""

class Pet:
    def __init__(self, name, happyness, life):
        self.name = name
        self.happyness = happyness
        self.life= life

    def play(self,value, game):
        self.happyness += value
        print (f"{self.name} is playing {game} ")
        print(f"{self.name}'s happyness is now {self.happyness}")
    
    def discard(self):
        self.life = False
        print(f"{self.name}'s happyness was {self.happyness} \n"
              "He dead now")

    def check(self):
        print(f"{self.name}'s happyness is currently {self.happyness}")


x= input("What would you like to name your pet? ")
x =Pet(f"{x}", 0, True)
x.check()

while x.life:
    isitem = False
    while not isitem:
        choice = input("\nWhat would you like to do?\n"
        "0: Play Fetch \n"
        "1: Check Stats \n"
        "2: Discard Pet").strip().lower()
        
        if choice in ["0", "play fetch", "fetch", "play", "0: Play Fetch"]:
            x.play(10, "Fetch")
        elif choice in ["1", "check stats", "check", "stats","1: Check Stats"]:
            x.check()
        elif choice in ["2", "discard", "discard pet", "discard of pet","2: Discard Pet"]:
            x.discard()
        else:
            print("Try again")