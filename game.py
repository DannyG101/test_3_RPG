import random

from core.player import Player
from core.orc import Orc
from core.goblin import Goblin


class Game:
    player_starts = False

    def __init__(self):
        self.player = Game.create_player()
        self.monster = Game.choose_random_monster()

    def start(self):
        player_roll = self.roll_dice(6) + self.player.speed
        monster_roll = self.roll_dice(6) + self.monster.speed
        if player_roll > monster_roll or player_roll == monster_roll:
            Game.player_starts = True
        self.show_menu()
        return Game.player_starts

    def run(self):
        self.start()

    def show_menu(self):
            user_input = input("please choose B for battle and E to exit and start the game again ").upper()
            if user_input == "B":
                self.battle(self.player, self.monster)
            else:
                self.start()

    def play(self):
        self.battle(self.player, self.monster)

    @staticmethod
    def create_player():
        return Player()

    @staticmethod
    def choose_random_monster():
        return random.choice((Orc(), Goblin()))

    def battle(self, player, monster):
        if Game.player_starts:
            print("Player's go")
            self.player.attack(self.monster)
            Game.player_starts = False
            if self.player.attack:
                damage = self.roll_dice(6) + self.player.power
                self.monster.hp -= damage
        else:
            print("Monster's go")
            self.monster.attack(self.player)
            Game.player_starts = True
            if self.player.attack:
                if self.monster.type == "knife":
                    damage = (self.roll_dice(6) + self.player.power) * 0.5
                    self.player.hp -= damage

                elif self.monster.type == "sword":
                    damage = self.roll_dice(6) + self.player.power
                    self.player.hp -= damage
                else:
                    damage = (self.roll_dice(6) + self.player.power) * 1.5
                    self.player.hp -= damage



    @staticmethod
    def roll_dice(sides):
        if sides == 20:
            return random.randint(1,20)
        else:
            return random.randint(1,6)

    def is_lost(self):
        if self.player.hp <= 0:
            print("Player lost")
            return True
        elif self.monster.hp <= 0:
            print("Monster lost")
            return True
        return False