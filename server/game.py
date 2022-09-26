class Game:
    _pixels: list[list[int]]

    def __init__(self, members: list, game_id: int):
        self._members = members
        self._id = game_id

    @property
    def members(self):
        return self._members

    @property
    def id(self):
        return self._id

    @property
    def pixels(self):
        return self._pixels

    def  __str__(self):
        pass