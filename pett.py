#Ways to kill: 1.Discard 2.Starve 3.Obestity 4.Depersion 5.Allery 6.Ignore 7.Cafine
class Pet:
   def __init__(self, name, happyness, life, hunger, allergy,ignoring,cafine):
       self.name = name
       self.happyness = happyness
       self.life= life
       self.hunger= hunger
       self.allergy = allergy
       self.ignoring= ignoring
       self.cafine= cafine
  
   def discard(self):
       self.life = False
       print(f"\n{self.name}'s dead now \n"
             f"{self.name}'s happyness was {self.happyness}")
       if self.hunger >20:
           print(f"{self.name}'s starved")
       elif self.hunger <= -5:
           print(f"{self.name} died from obeisty")
       elif self.happyness < -5:
            print(f"{self.name} died from depersion")
       elif self.allergy == True:
            print(f"{self.name} died from allergy")
       elif self.ignoring >=3:
            print(f"{self.name} died from ignorace")
       elif self.cafine== True:
           print(f"{self.name} died from cafine")

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

alleric=["apple","chocolate", "samsung tv", "pollen", "cats", "food", "The Double Ristretto Venti Half-Soy Nonfat Decaf Organic Chocolate Brownie Iced Vanilla Double-Shot Gingerbread Frappuccino"]

import random
x= input("What would you like to name your pet? ")
x =Pet(f"{x}", 0, True, 10, False,0,False)
x.check()
inplay =False
while x.life:
   isitem = False
   while not isitem:
       choice = input("\nWhat would you like to do?\n"
       "0: Play \n"
       "1: Check Stats \n"
       "2: Discard Pet \n"
       "3: Feed \n"
       "4: Ignore\n").lower()

       if choice in ["0", "play", "0: Play"]:
           inplay =True
           y = input("What Game? ")
           x.play(10, y)
           if x.hunger > 20:
                x.discard()
                break
           inplay =False
       elif choice in ["1", "check stats", "check", "stats","1: Check Stats"]:
           x.check()
       elif choice in ["4","ignore", "4: Ignore"]:
           x.ignoring+= 1
           x.hunger =+ 2
           x.happyness =- 2
           if x.ignoring >=3:
               x.discard()
               break
       elif choice in ["3", "feed","3: Feed"]:
           z = input("What Food? ")
           if z.lower()== "Cafine" or z.lower() == "The Double Ristretto Venti Half-Soy Nonfat Decaf Organic Chocolate Brownie Iced Vanilla Double-Shot Gingerbread Frappuccino":
               x.cafine=True
               x.discard ()
               break
           for i in alleric:
              if z.lower == i: 
                   allery = True
                   x.discard
                   break
           x.feed(7, z)
           if x.hunger < -5:
                x.discard()
                break
       elif choice in ["2", "discard", "discard pet", "discard of pet","2: Discard Pet"]:
           x.discard()
           break
       else:
           print("Try again")
       r = random.randint(1, 10)
       a = random.randint(1, 10)
        
       if r <= 2 and x.life and not inplay:
           x.hunger =+ r
           print(f"\n{x.name} randomly got hunger increased by {r}")
           if x.hunger < 0:
                x.discard()
                break
       if a <= 2 and x.life and not inplay:
           inplay =True
           x.happyness =- a
           print(f"\n{x.name} randomly got happyness decreased by {a}")
           if x.happyness <= -5:
                x.discard()
                break
           inplay =False

