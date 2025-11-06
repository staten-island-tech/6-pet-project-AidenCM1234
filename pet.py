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

    def play(self,game):
        self.happyness += game
        print (f"{self.name} is playing {game}")
        print(f"{self.name}'s happyness is now {self.happyness}")
    
    def discard(self):
        self.life = False
        print(f"{self.name}'s happyness was {self.happyness}")

    def check(self):
        print(f"{self.name}'s happyness is currently {self.happyness}")


x= input("What would you like to name your pet? ")
x =Pet(f"{x}", 0, True)
x.check()
#while self.life == True:

life=True

while life:
    isthing = False
    while not isitem:
        choice = input("Please choose one item to purchase: ")
        
        for item in store:
            if choice == item["name"]: 
                print(f"You have purchased one {item['name']} for ${item['price']}")
                cart.append(f"{item['name']} - ${item['price']}")
                total+=item['price']
                isitem = True
        
        if not isitem:  
            print("Try again")
    a=False
    while not a:
        again = input("Would you like to purchase more items? (Y/N): ")
        if again == 'N':
            done = True
            a=True 
        elif again == 'Y':
            a=True
        elif again != 'N' or 'Y':
            print("Try again")


    