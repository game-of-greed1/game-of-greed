from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self):
        self.banker=Banker()
    
    def play(self,roller=None):
        self.roller=roller or GameLogic.roll_dice
        print("Welcome to Game of Greed")
        user_input = input("(y)es to play or (n)o to decline")
        if user_input =="y" or user_input=="yes":
          self.game()

        else :
         print("OK. Maybe another time")
      

 