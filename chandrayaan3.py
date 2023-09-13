# In chandrayaan3.py

class Chandrayaan3:
    def __init__(self):
        self.position = [0, 0, 0]
        self.direction = 'N'

    def move(self, command):
        if command == 'f':
            self.position[1] += 1
        elif command == 'b':
            self.position[1] -= 1

    def turn(self, command):
        if command == 'l':
            if self.direction == 'N':
                self.direction = 'W'
            

    def tilt(self, command):
        if command == 'u':
            if self.direction == 'N':
                self.direction = 'U'
            

    def getPosition(self):
        return self.position

    def getDirection(self):
        return self.direction
