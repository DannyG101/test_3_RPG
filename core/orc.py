import random

import game


class Orc:
    def __init__(self):
        self.name = "Mark"
        self.hp = 50
        self.type = "orc"
        self.speed = random.randint(0,5)
        self.power = random.randint(10,15)
        self.armor_rating = random.randint(2, 8)
        self.weapon = random.choice(["knife", "sword", "axe"])

    def speak(self):
        print(f"{self.type} {self.name} is ANGRY!!")

    def attack(self, other):
        turn = game.Game.roll_dice(20) + self.speed
        if turn > other.armor_rating:
            return True
        else:
            return False