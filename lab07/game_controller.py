# game_controller.py
from pair_of_dice import PairOfDice


class GameController:
    def __init__(self):
        self.dice = PairOfDice()
        self.point = None

    def roll_and_check(self):
        roll = self.dice.roll_dice()
        print(f"You rolled {roll}.")
        if self.point is None:  # First roll
            if roll == 7 or roll == 11:
                print("You win!")
                return True
            elif roll == 2 or roll == 3 or roll == 12:
                print("You lose.")
                return True
            else:
                self.point = roll
                print(f"Your point is {self.point}.")
                return False
        else:  # Subsequent rolls
            if roll == self.point:
                print("You win!")
                return True
            elif roll == 7:
                print("You lose.")
                return True
            return False

    def play_game(self):
        game_over = False
        while not game_over:
            input("Press enter to roll the dice...")
            game_over = self.roll_and_check()
