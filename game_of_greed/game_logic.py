import random

from collections import Counter
from random import randint

roles={
    (1,1):100,(5,1):50,(1,3):1000,(1,4):2000,(1,5):3000,(1,6):4000,(2,3):200,(2,4):400,(2,5):600,(2,6):800,(3,3):300,(3,4):600,(3,5):900,(3,6):1200,(4,3):400,(4,4):800,(4,5):1200,(4,6):1600,(6,6):2400,(6,5):1800,(6,4):1200,(6,3):600,(5,6):2000,(5,5):1500,(5,4):1000,(5,3):500,(1,2):200,(2,2):0,(3,2):0,(4,2):0,(5,2):100,(6,2):0,(2,1):0,(3,1):0,(4,1):0,(6,1):0,
}

######################################################################
######################################################################

class GameLogic:

    @staticmethod
    def calculate_score(dice_roll:tuple)->int:
        score=0
        count_times =Counter(dice_roll).most_common()
        hot_dice=sorted(dice_roll)
        if hot_dice==[1,2,3,4,5,6]:
            score=1500
            return score
        elif len(count_times )==3 and count_times [2][1] == 2:
            score=1500
            return score
        for x in count_times :
            score+=roles[x]
        return score

######################################################################

    @staticmethod
    def roll_dice(num):
        list = [random.randint(1,6) for i in range(num)]
        return tuple(list)

######################################################################

    @staticmethod   
    def validate_keepers(roll,keeper):
        roll=Counter(roll).most_common()
        keeper=Counter(keeper).most_common()

        if len(keeper)>len(roll):
                return False
        
        for i in keeper:
            if i not in roll:
                return False

        if len(keeper)==3 and keeper[2][1] == 2:
            return True

        for i in keeper:
            if roles[i] ==0:
                return False
        return True
        
######################################################################

    @staticmethod
    def get_scorers(test_input):
        result=[]
        count = Counter(test_input).most_common()
        for i in count:
            if roles[i] !=0:
                for x in range(i[1]) :
                    result.append(i[0])
        return tuple(result)
