# src/LaswerWeaponArmory.py

from random import randint
from .scene import Scene
from .util import dd


class LaserWeaponArmory(Scene):

    def enter(self):
        dd("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding. It's dead
            quiet, too quiet. You stand up and run to the far side of
            the room and find the neutron bomb in it's container.
            There's a keypad lock on the box and you need the code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
            """)

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            dd("""
                The container clicks open and seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the
                right spot.
                """)

        else:
            dd("""
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                together. You decide to sit there, and finally the
                Gothons blow up the ship from their ship and you die.
                """)
            return 'death'
