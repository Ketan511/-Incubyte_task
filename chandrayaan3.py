# In chandrayaan3.py

class Chandrayaan3:
    def __init__(self):
        self.position = [0, 0, 0]
        self.direction = 'N'

    def move(self, command, dir):
        if command == 'f':
            if dir == 'N':
                self.position[1] += 1
            elif dir == 'S':
                self.position[1] -= 1
            elif dir == 'E':
                self.position[0] += 1
            elif dir == 'W':
                self.position[0] -= 1
            elif dir == 'U':
                self.position[2] += 1
            elif dir == 'D':
                self.position[2] -= 1
        elif command == 'b':
            if dir == 'N':
                self.position[1] -= 1
            elif dir == 'S':
                self.position[1] += 1
            elif dir == 'E':
                self.position[0] -= 1
            elif dir == 'W':
                self.position[0] += 1
            elif dir == 'U':
                self.position[2] -= 1
            elif dir == 'D':
                self.position[2] += 1
    
    def turn(self, command, dir):
        if command == 'l':
            if dir == 'N':
                self.direction = 'W'
            elif dir == 'S':
                self.direction = 'E'
            elif dir == 'E':
                self.direction = 'N'
            elif dir == 'W':
                self.direction = 'S'
            elif dir == 'U':
                self.turn(command, self.prev)  # Use previous direction
            elif dir == 'D':
                self.turn(command, self.prev)
        elif command == 'r':
            if dir == 'N':
                self.direction = 'E'
            elif dir == 'S':
                self.direction = 'W'
            elif dir == 'E':
                self.direction = 'S'
            elif dir == 'W':
                self.direction = 'N'
            elif dir == 'U':
                self.turn(command, self.prev)
            elif dir == 'D':
                self.turn(command, self.prev)
            

    def tilt(self, command):
        if command == 'u':
            if self.direction == 'N':
                self.direction = 'U'
            

    def getPosition(self):
        return self.position

    def getDirection(self):
        return self.direction
