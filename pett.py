
class Pet:
   def __init__(self, name, happyness, life, hunger):
       self.name = name
       self.happyness = happyness
       self.life= life
       self.hunger= hunger
  
   def discard(self):
       self.life = False
       print(f"{self.name}'s happyness was {self.happyness} \n"
             f"{self.name}'s dead now")
  

   def play(self,value, game):
       self.happyness += value
       self.hunger += value
       print (f"{self.name} is playing {game} ")
       print(f"{self.name}'s happyness is now {self.happyness}")
       print(f"{self.name}'s hunger is now {self.hunger}")
       
   def feed(self,value, food):
       self.hunger -= value
       print (f"{self.name} is eating {food} ")
       print(f"{self.name}'s hunger is now {self.hunger}")

   def check(self):
       print(f"{self.name}'s happyness is currently {self.happyness}")
       print(f"{self.name}'s hunger is currently {self.hunger}")


x= input("What would you like to name your pet? ")
x =Pet(f"{x}", 0, True, 10)
x.check()

while x.life:
   if x.hunger > 20:
       x.discard()
   isitem = False
   while not isitem:
       choice = input("\nWhat would you like to do?\n"
       "0: Play \n"
       "1: Check Stats \n"
       "2: Discard Pet \n"
       "3: Feed \n").lower()
      
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
           x.feed(10, z)
       elif choice in ["2", "discard", "discard pet", "discard of pet","2: Discard Pet"]:
           x.discard()
           break
       else:
           print("Try again")
