
class Pet:
   def __init__(self, name, happyness, life, hunger):
       self.name = name
       self.happyness = happyness
       self.life= life
       self.hunger= hunger
  
   def discard(self):
       self.life = False
       print(f"{self.name}'s dead now \n"
             f"{self.name}'s happyness was {self.happyness} \n")
       if self.hunger >20:
           (f"{self.name}'s starved")
       if self.hunger <0:
           (f"{self.name} died from obeisty")
  

   def play(self,value, game):
       self.happyness += value
       self.hunger += value
       print (f"{self.name} is playing {game} \n"
            f"{self.name}'s happyness is now {self.happyness}\n"
            f"{self.name}'s hunger is now {self.hunger}")
       
   def feed(self,value, food):
       self.hunger -= value
       print (f"{self.name} is eating {food} ")
       print(f"{self.name}'s hunger is now {self.hunger}")

   def check(self):
       print(f"{self.name}'s happyness is currently {self.happyness}")
       print(f"{self.name}'s hunger is currently {self.hunger}")


import random

x= input("What would you like to name your pet? ")
x =Pet(f"{x}", 0, True, 10)
x.check()

while x.life:
   isitem = False
   while not isitem:
       r = random.randint(1, 10)
       a = random.randint(1, 10)
       choice = input("\nWhat would you like to do?\n"
       "0: Play \n"
       "1: Check Stats \n"
       "2: Discard Pet \n"
       "3: Feed \n").lower()
       if r <= 2 and x.life:
           x.hunger =+ r
           print(f"{x.name} randomly got hunger increased by {r}")
           if x.hunger < 0:
                x.discard()
                break
       if a <= 2 and x.life:
           x.happyness =- a
           print(f"{x.name} randomly got happyness decreased by {a}")

       if choice in ["0", "play",  "play", "0: Play"]:
           y = input("What Game? ")
           x.play(10, y)
           if x.hunger > 20:
                x.discard()
                break
       elif choice in ["1", "check stats", "check", "stats","1: Check Stats"]:
           x.check()
       elif choice in ["3", "feed","3: Feed"]:
           z = input("What Food? ")
           if x.hunger < 0:
                x.discard()
                break
       elif choice in ["2", "discard", "discard pet", "discard of pet","2: Discard Pet"]:
           x.discard()
           break
       else:
           print("Try again")
