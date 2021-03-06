# src/EscapePod.py

from random import randint
# our lib
from .util import dd
from .scene import Scene

class EscapePod(Scene):

    def enter(self):
        dd("""
        You rush through the ship desperately trying to make it to
        the escape pod before the whole ship explodes. It seems
        like hardly any Gothons are on the ship, so your run is
        clear of interference. You get to the chamber with the
        escape pods, and now need to pick one to take. Some of
        them could be damaged but you don't have time to look.
        There's 5 pods, which one do you take?
        """)

        good_pod = randint(1,5)
        guess = input("[pod]> ")

        if int(guess) != good_pod:
            dd("""
            You jump into pod {guess} and hit the eject button.
            The pod escape out into the void of space, then
            implodes as the hull ruptures, crushing your body
            into jam jelly.
            """)

            return 'death'

        else:
            dd("""
            You jump into pod {guess} and hit the eject button.
            The pod easily slides out into space heading to
            the planet below. As it flies to the planet, you look
            back and see your ship implode then explode like a
            bright start, taking out the Gothon ship at the same
            time. You won!
            """)

            return 'finished'
