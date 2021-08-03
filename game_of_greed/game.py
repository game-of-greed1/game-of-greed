from typing import Container
# from game_of_greed import game_logic
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter


class Game(GameLogic, Banker): 

    def play(self, roller=None):
        roller=roller or Game.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        ask_User = input("> ")

        if ask_User == "y":
            in_play = True
            rounds_number = 1
            dice_number = 6
            ask_User2 = "b"
            while in_play:
                if ask_User2 == "b":
                    print(f"Starting round {rounds_number}")
                print(f"Rolling {dice_number} dice...")
                dice = roller(dice_number)
                Game.print_random_dice(dice)
                print("Enter dice to keep, or (q)uit:")
                keep_or_leave = input("> ") 
                if keep_or_leave == "q":
                    in_play = False
                    print(f"Thanks for playing. You earned {self.balance} points")
                else:
                    dice_value = []
                    for x in keep_or_leave:
                        dice_value.append(int(x))
                    tuple_list = tuple(dice_value)
                    temp_shelf = self.calculate_score(tuple_list)
                    self.shelf(temp_shelf)
                    dice_number = dice_number - len(keep_or_leave) 
                    print(f"You have {self.shelved} unbanked points and {dice_number} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    ask_User2 = input("> ")
                    if ask_User2 == "r":
                        continue
                    elif ask_User2 == "b":
                        print(f"You banked {self.shelved} points in round {rounds_number}")
                        self.bank()
                        rounds_number += 1
                        print(f"Total score is {self.balance} points")
                        dice_number = 6
                    elif ask_User2 == "q":
                        print(f"Thanks for playing. You earned {self.balance} points")
                        in_play = False
        else: 
            print("OK. Maybe another time")
    

    @staticmethod
    def print_random_dice(dice):
        first_string = "*** "
        last_string = "***"
        for x in dice:
            first_string = first_string + str(x) + " " 
        first_string+=last_string
        print(first_string)


    def zilch(self, round_number):
        print('****************************************')
        print('**        Zilch!!! Round over         **')
        print('****************************************')
        print(f"You banked 0 points in round {round_number}")           
        print(f"Total score is {self.balance} points")
        self.round_number+=1
        self.dice_number = 6


if __name__ == "__main__":
    game = Game()
    game.play()
