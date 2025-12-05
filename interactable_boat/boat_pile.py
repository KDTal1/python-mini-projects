import random

class Boat(): #making the boat
    def __init__(self, name, speed): # make boat, initialize descriptions for boat (speed determines whether, fast, normal, slow)
         self.name = name
         self.speed = str(speed)
         self.score = 0

         #only three selections "fast", "normal", "slow"
         match self.speed:
              case "fast":
                   self.speed_int = 15
              case "normal":
                   self.speed_int = 10
              case "slow":
                   self.speed_int = 5
              case _:
                   self.speed_int = 0 # if user wrote invalid initial speed

    def add_score(self): # adds score for boat
         if not self.speed_int < 0:
              self.score += 0

         self.score += int(self.speed_int * 0.5)
         print(f"Score added to {self.name}")

    def change_speed(self, inc_dec=None, num=None): # changes the speed depending on the user's decision
         if not num: # default value if num is with no value
              num = 1

         if not inc_dec:
              self.speed_int = self.speed_int

         if inc_dec == "increment":
              self.speed_int += num
         elif inc_dec == "decrement":
              self.speed_int += -num
         elif inc_dec == "stop":
              self.speed_int = 0
              

    def show_info(self): #prints info of the boat.
         print(f"{self.name}\n* Selected Speed: {self.speed}\n* Current Speed (num): {self.speed_int}\n* Score: {self.score}")\

class AutoBoat(Boat): # making the boat, automated version
     def __init__(self, name, speed):
          super().__init__(name, speed)

     def update_move(self):
          choices = [
               lambda: self.change_speed("increment", random.randint(1, 5)),
               lambda: self.change_speed("decrement", random.randint(1, 5))
          ]
          
          random.choice(choices)()

class Rock(): #now make the rock
     def __init__(self, size):
        self.size = size
     
     def damage_inflict(self): #rock returns damage
        damage = int(self.size * (random.randint(1, 5) / 10))

        return damage