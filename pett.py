#Ways to kill: 1.Discard 2.Starve 3.Obestity 4.Depersion 5.Ignore 6.Cafine
class Pet:
   def __init__(self, name, happyness, life, hunger, ignoring,cafine,turns):
       self.name = name
       self.happyness = happyness
       self.life= life
       self.hunger= hunger
       self.ignoring= ignoring
       self.cafine= cafine
       self.turns=turns
  
   def discard(self):
       self.life = False
       print(f"\n{self.name}'s dead now \n"
             f"{self.name}'s happyness was {self.happyness}\n"
             f"You killed your pet in {self.turns} Turns")

       if self.hunger >20:
           print(f"{self.name}'s starved")
       elif self.hunger <= -5:
           print(f"{self.name} died from obeisty")
       elif self.happyness < -5:
            print(f"{self.name} died from depersion")
       elif self.ignoring >=3:
            print(f"{self.name} died from rejeshion")
       elif self.cafine== True:
           print(f"{self.name} died from cafine")

   def play(self,value, game):
       self.happyness += value
       self.hunger += value
       print (f"{self.name} is playing {game} \n"
            f"{self.name}'s happyness is now {self.happyness}\n"
            f"{self.name}'s hunger is now {self.hunger}\n")
       
   def feed(self,value, food):
       self.hunger -= value
       print (f"{self.name} is eating {food} ")
       print(f"{self.name}'s hunger is now {self.hunger}")

   def check(self):
       print(f"{self.name}'s happyness is currently {self.happyness}")
       print(f"{self.name}'s hunger is currently {self.hunger}")
       print(f"Turn: {self.turns}")

   def take_turn(self,turns):
       turns +=1

   def four(self, ignoring, hunger, happyness):
        self.ignoring+= 1
        self.hunger += 2
        self.happyness -= 2

   def hungerr(self,value):
       self.hunger +=value
       #print(f"\n{self.name} randomly got hunger increased by {value}")
   def hungera(self,value):
       self.hunger +=value
       #print(f"\n{self.name} randomly got hunger increased by {value}")

import random
x= input("What would you like to name your pet? ")
x =Pet(f"{x}", 0, True, 10,0,False,0)
x.check()
inplay =False
h=False
d=False
print("Your Goal: Keep your pet alive For 10+ Turns OR it dies in the most intersting ways\n" \
"Your pets Happyness and Hunger will randomly change so keep on checking\n" \
"Choose (2: Discard Pet) to quit")
while x.life and d==False:
   isitem = False
   while not isitem and not d:
       choice = input("\nWhat would you like to do?\n"
       "0: Play \n"
       "1: Check Stats \n"
       "2: Discard Pet \n"
       "3: Feed \n"
       "4: Ignore\n").lower()
       choice =choice.strip()
       if choice not in ["1", "check stats", "check", "stats","1: Check Stats"]:
        x.take_turn
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
           x.four(x.ignoring,x.hunger, x.happyness)
           if x.ignoring >=3:
               x.discard()
               break
       elif choice in ["3", "feed","3: Feed"]:
           z = input("What Food? ")
           if z.lower()== "cafine" or z.lower() == "the double ristretto venti half-soy nonfat decaf organic chocolate brownie iced vanilla double-shot gingerbread frappuccino":
               x.cafine=True
               x.discard () 
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
       while h == False and x.turns>=10:
        if x.turns>=10:
           x.winner()
           print ("You won HE surived >=10 turns")
           c =input("would you like to couintue: Yes or No ")
           if c.lower() =="no" or c.lower() =="n":
               print("You said NO")
               d=True
               break
           elif c.lower() == "yes" or c.lower()=="y":
               print("You said YES")
               print("To end just discard pet")
               h =True
           else:
               print("try again")

       r = random.randint(1, 10)
       a = random.randint(1, 10)
        
       if r <= 2 and x.life and not inplay:
           x.hungerr(r)
           if x.hunger < 0:
                x.discard()
                break
       if a <= 2 and x.life and not inplay:
           inplay =True
           x.happynessa() =- a
           #print(f"\n{x.name} randomly got happyness decreased by {a}")
           if x.happyness <= -5:
                x.discard()
                break
           inplay =False