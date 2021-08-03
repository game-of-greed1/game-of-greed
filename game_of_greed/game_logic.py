import random

from collections import Counter
from random import randint
class GameLogic:

    @staticmethod
    def roll_dice(num):
        list = [random.randint(1,6) for i in range(num)]
        return tuple(list)

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



