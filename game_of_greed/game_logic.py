
import random


@staticmethod
def roll_dice(num):
  list = [random.randint(1,6) for i in range(num)]
  return tuple(list)





