

from .scene import Scene

class Finished(Scene):

    def enter(self):
        print("You wont! Good job.")
        return 'finished'
