import random

import game


class Player:
    def __init__(self):
        self.name = "Danny"
        self.hp = 50
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)
        self.armor_rating = random.randint(5, 15)
        self.profession = random.choice(["fighter", "healer"])
        if self.profession == "fighter":
            self.power += 2
        else:
            self.hp += 10

    def speak(self):
        print(f"my name is: {self.name} and I'm ready!!")

    def attack(self, other):
        turn = game.Game.roll_dice(20) + self.speed
        if turn > other.armor_rating:
            return True
        else:
            return False
