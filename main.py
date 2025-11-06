
from game import Game
if __name__ == "__main__":
    my_game = Game()

    while not my_game.is_lost():
        my_game.start()