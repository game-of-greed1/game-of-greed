import random

from collections import Counter
from random import randint


class GameLogic:

    ####################################################################

    @staticmethod
    def roll_dice(num):
        list = [random.randint(1,6) for i in range(num)]
        return tuple(list)

    ####################################################################

    @staticmethod
    def calculate_score(dice):
       
        if len(dice) > 6:
            raise Exception("Cheating Cheater!")

        count_times = Counter(dice)

        if len(count_times) == 6:
            return 1500

        if len(count_times) == 3 and all(val == 2 for val in count_times.values()):
            return 1500

        score = 0

        ones_used = fives_used = False

        for num in range(1, 6 + 1):

            pip_count = count_times[num]

            if pip_count >= 3:

                if num == 1:

                    ones_used = True

                elif num == 5:

                    fives_used = True

                score += num * 100

                
                pips_beyond_3 = pip_count - 3

                score += score * pips_beyond_3

             
                if num == 1:
                    score *= 10

        if not ones_used:
            score += count_times.get(1, 0) * 100

        if not fives_used:
            score += count_times.get(5, 0) * 50

        return score

    ############################################################

    def validate_keepers(arr1 , arr2):
        arr1 = Counter(arr1)
        arr2 = Counter(arr2)
        for key in arr1:
            if key in arr2:
                if(arr1[key] == arr2[key]):
                    return True
                else:
                    return False
            else:
                return False

    ####################################################################

    @staticmethod
    def get_scoqrers(dice):
        all_dice_score = GameLogic.calculate_score(dice)

        print(f'all_dice_score >>>>> {all_dice_score}')

        if all_dice_score == 0:
            return tuple()

        scorers = []
        for i in range(len(dice) + 1 ):
            sub_roll = dice[:i] + dice[i + 1 :]
            print(f'sub_roll > {sub_roll} /  i > {i}')
            sub_score = GameLogic.calculate_score(sub_roll)
            print(f'sub_score > {sub_score} /  i > {i}')
            if sub_score != all_dice_score:
                scorers.append(dice[i])
                print(f'End if')
            print("*******************************************")
        print(f'scorers > {scorers}')
        return tuple(scorers)



############################################################

if __name__ == "__main__":
    game = GameLogic()
    test = game.get_scoqrers( (4, 5, 2, 3, 3, 6,) )
    print("###################")
    print(test)
    print("###################")
    # print(test)
    # print("***********************")
    # dice = ( 2, 2, 3, 3, 3, 6, )
    # print(len(dice))
    # print("***********************")
    # scorers = []
    # for i in range(len(dice) ):
    #     sub_roll = dice[:i] + dice[i + 1 :]
    #     sub_score = GameLogic.calculate_score(sub_roll)
    #     if sub_score != all_dice_score:
    #         scorers.append(dice[i])
        
