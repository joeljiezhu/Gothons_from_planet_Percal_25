# src/Death.py

from sys import exit
from random import randint
from .scene import Scene

class Death(Scene):
    quips = [
        "You died. You kinda suck at this",
        "Your mom would be proud ... if she were smarter",
        "Such a loser",
        "I have a small puppy that's better at this",
        "You're worse than your Dad's jokes"
    ]


    def enter(self):
        # @NOTE why is the first call is static?
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exixt(1)
