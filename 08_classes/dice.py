from random import randint


class Dice:
    """Throw dice class"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self, roll_times):
        self.roll_times = roll_times
        roll = 0
        while roll < self.roll_times:
            print(randint(1, self.sides))
            roll += 1


dice6 = Dice()
dice6.roll_dice(10)
print()

dice10 = Dice(10)
dice10.roll_dice(10)
print()

dice20 = Dice(20)
dice20.roll_dice(10)