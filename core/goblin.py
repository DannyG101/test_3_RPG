import random

import game


class Goblin:
    def __init__(self):
        self.name = "Joe"
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)
        self.armor_rating = 1
        self.weapon = random.choice(["knife", "sword", "axe"])

    def speak(self):
        print(f"{self.type} {self.name} is ANGRY!!")

    def attack(self, other):
        turn = game.Game.roll_dice(20) + self.speed
        if turn > other.armor_rating:
            return True
        else:
            return False