class Debugger:

    def __init__(self, active):
        self.active = active

    def print(self, message):
        if self.active:
            print(message)