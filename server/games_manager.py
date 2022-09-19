from game import Game


class GamesManager:
    _id_counter: int

    def __init__(self):
        self._id_counter = 0

    def create_new_game(self, members):
        new_game = Game(members, self._id_counter)
        self._id_counter += 1
        return new_game
