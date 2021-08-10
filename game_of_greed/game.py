from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game(GameLogic, Banker): 

    def play(self, roller=None):
        roller=roller or Game.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        ask_User = input("> ")

        if ask_User == "y":
            in_play  = True
            rounds_number  = 1
            dice_number  = 6
            if rounds_number  !=20:
                print(f"Starting round {rounds_number }")
            while in_play :
                if rounds_number  == 20:
                    self.bank()
                    print(f"Thanks for playing. You earned {self.balance} points")
                    break

                print(f"Rolling {dice_number } dice...")
                dice = roller(dice_number )

                first_string = "*** "
                for x in dice:
                    first_string = first_string + str(x) + " "
                first_string = first_string + "***"
                print(first_string)

                if  not Game.get_scorers(dice):
                    
                    print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
                    print(f"You banked {0} points in round {rounds_number }")
                    print(f"Total score is {self.balance} points")
                    dice_number =6
                    rounds_number +=1
                    print(f"Starting round {rounds_number }")

                    continue
                    


                print("Enter dice to keep, or (q)uit:")
                keep_or_leave  = input("> ") 
                keep_or_leave = keep_or_leave .replace(' ', '')
                if keep_or_leave  == "q" or rounds_number ==20:
                    in_play  = False
                    print(f"Thanks for playing. You earned {self.balance} points")
                else :
                    
                   
                    keep_or_leave =[int(i) for i in keep_or_leave  ]
                    while not Game.validate_keepers(dice,tuple(keep_or_leave )) and in_play : 
                        print("Cheater!!! Or possibly made a typo...")
                        print(first_string)
                        print("Enter dice to keep, or (q)uit:")
                        keep_or_leave =input("> ")
                        keep_or_leave = keep_or_leave .replace(' ', '')
                        if keep_or_leave =="q" or rounds_number ==20:
                            in_play =False
                        else:
                            

                            keep_or_leave = [int(i) for i in keep_or_leave  ]

                    if keep_or_leave =="q" or rounds_number ==3:
                        print(f"Thanks for playing. You earned {self.balance} points")
                        continue
                    if len(keep_or_leave )==dice_number :
                        shelf_score =1500
                    else:
                        shelf_score = self.calculate_score(keep_or_leave )

                    self.shelf(shelf_score)
                    dice_number  = dice_number  - len(keep_or_leave ) 
                    print(f"You have {self.shelved} unbanked points and {dice_number } dice remaining")
                    if dice_number ==0:
                        dice_number =6
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    ask_User2 = input("> ")
                    while ask_User2!="r" and ask_User2!="b" and ask_User2!="q":
                        print("please enter the correct input")
                        print("(r)oll again, (b)ank your points or (q)uit:")
                        ask_User2 = input("> ")
                        
                    if ask_User2 == "q" or rounds_number ==20 :
                        print(f"Thanks for playing. You earned {self.balance} points")
                        in_play  = False
                    elif ask_User2 == "b":
                        print(f"You banked {self.shelved} points in round {rounds_number }")
                        self.bank()
                        rounds_number  += 1
                        print(f"Total score is {self.balance} points")

                        dice_number  = 6
                        if rounds_number !=20:
                            print(f"Starting round {rounds_number }")

                    elif ask_User2 == 'r':
                        continue
                    
                    
        else: 
            print("OK. Maybe another time")

    
######################################################################
######################################################################

if __name__ == "__main__":
    game = Game()
    game.play()
