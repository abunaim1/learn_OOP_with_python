class School:
    def __init__(self, address) -> None:
        self.address = address

class Sprots:
    def __init__(self, game) -> None:
        self.game = game

class Family:
    def __init__(self, lives) -> None:
        self.lives = lives

class Student(Family, Sprots, School):
    def __init__(self, address, game, lives) -> None:
        School.__init__(self, address)
        Sprots.__init__(self, game)
        Family.__init__(self, lives)