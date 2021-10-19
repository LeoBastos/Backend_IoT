class Modules:
    """ Config Modules with Injection """

    def __init__(self, make):
        self.make = make

    def make_action(self):
        self.make.action()
