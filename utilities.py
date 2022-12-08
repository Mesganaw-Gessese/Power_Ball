# ues to 'random' because of the system choose 5 numbers randomly
import random
# 'colorama' uses for colored strings.  use to this because the output will be colored.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# This Function Uses to choose 5 numbers randomly for 'winning white balls' and 'lucky white balls' by using 'sample'.
#
def RandomForWhiteBalls():
    # RandomNumber = random.randint(1,20)
    RandomNumber = random.sample(range(1, 20), k = 5)
    return (RandomNumber)

# This Function Uses to choose 1 numbers randomly for 'winning golden balls' and 'lucky golden balls' by using 'randint'
def RandomForPowerBalls():
    RandomNumber = random.randint(1,10)
    return (RandomNumber)


class WinningWhiteBalls():

    def __init__(self, number1):
        self.number1 = number1

class WinningGoldenBall():

    def __init__(self, golden):
        self.golden = golden

Winning_WhiteBall =WinningWhiteBalls(RandomForWhiteBalls())
Wi_GoldenBall = WinningGoldenBall(RandomForPowerBalls())
winnerAscending = Winning_WhiteBall.number1
winnerAscending.sort()
# '\33[1m', '\33[34m' and '\33[0m', they uses colored and bold strings.
print("\33[1m\33[34m Today's Powerball Winning Numbers:\33[0m")
print(Fore.LIGHTMAGENTA_EX + str(Winning_WhiteBall.number1), Fore.YELLOW + str(Wi_GoldenBall.golden))

class LuckyWhiteBalls():

    def __init__(self, number1):
        self.number1 = number1

class LuckyGoldenBall():

    def __init__(self, golden):
        self.golden = golden

Lu_WhiteBall = LuckyWhiteBalls(RandomForWhiteBalls())
Lu_GoldenBall = LuckyGoldenBall( RandomForPowerBalls())
LuckyAscending = Lu_WhiteBall.number1
LuckyAscending.sort()
# '\33[1m', '\33[34m' and '\33[0m', they uses colored and bold strings.
print("\33[1m\33[34mYour Lucky Numbers:\33[0m")
print(Fore.LIGHTMAGENTA_EX + str(Lu_WhiteBall.number1), Fore.YELLOW + str(Lu_GoldenBall.golden))