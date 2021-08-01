

class GameLogic:

    @staticmethod
    def calculate_score(num)->int:

        if( num.count(5) == 3):
            return 500  
        
        if( num.count(1) == 3 and  num.count(5) == 1 ):
            return 1050  

        if( num.count(1) == 3):
            return 1000 

           


        if(num[0] == 5):
         num = num * 10
         result = sum(num)
         return result

        if(num[0] == 1 ):
         num = num * 100
         result1 = sum(num)
         return result1

        if(num[0] == 5 and num[1]==5):
         num = num * 10
         result = sum(num)
         return result

        if(num[0] == 1 and num[1]==1):
         num = num * 100
         result = sum(num)
         return result 

           #(1,5)
        # if(num[0] == 1 and num[1]==5):
        #  num1 = num[0] * 100
        #  num2 = num[1] * 10
        #  result1 = sum(num1)
        #  result2 = sum(num2)
        #  final = result1 +result2
        #  return result 

        if(num[0] == 2):
         num = num * 0
         result = sum(num)
         return result

        if( num.count(5) == 3):
            return 500  

         






