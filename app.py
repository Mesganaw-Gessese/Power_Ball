# 'from utilities import *' uses this code because of  import all cods from utilities.
from utilities import *



class WinningValue():
   counterWhite = 0
   for i in Lu_WhiteBall.number1:
       if i in Winning_WhiteBall.number1:
           counterWhite = counterWhite + 1

   if (counterWhite) == 5 and (Wi_GoldenBall.golden == Lu_GoldenBall.golden):
       print(counterWhite,"correct white balls and  power ball: $ 324,000,000")
   elif (counterWhite) == 5 and (Wi_GoldenBall.golden != Lu_GoldenBall.golden):
       print(counterWhite,"correct white balls and no power ball: $ 1,000,000")
   elif (counterWhite) == 4 and (Wi_GoldenBall.golden == Lu_GoldenBall.golden):
       print(counterWhite, "correct white balls and  power ball: $ 10,000")
   elif counterWhite == 4 and (Wi_GoldenBall.golden != Lu_GoldenBall.golden):
       print(counterWhite, "correct white balls and no power ball: $ 100")
   elif counterWhite == 3 and (Wi_GoldenBall.golden == Lu_GoldenBall.golden):
       print(counterWhite, "correct white balls and power ball: $ 100")
   elif counterWhite == 3 and (Wi_GoldenBall.golden != Lu_GoldenBall.golden):
       print(counterWhite, "correct white balls and no power ball: $ 7")
   elif counterWhite == 2 and (Wi_GoldenBall.golden == Lu_GoldenBall.golden):
       print(counterWhite, "correct white balls and power ball: $ 7")
   elif (counterWhite )== 1 and (Wi_GoldenBall.golden == Lu_GoldenBall.golden):
       print(counterWhite, "correct white balls and power ball: $ 4")
   elif (counterWhite) == 0 and (Wi_GoldenBall.golden == Lu_GoldenBall.golden):
       print("No White Balls, Just the Powerball: $ 4")
   else:
       print("try again!")

