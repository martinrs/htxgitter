import random
import string

class World():

    def __init__(self):
        self.currentRoom = Room()

    def newRoom(self, entryDirection):
        self.currentRoom = Room(self.currentRoom.contents[entryDirection], entryDirection)

class Room():

    doorChance = 0.15
    directions = ['nord', 'syd', 'øst', 'vest', 'op', 'ned']

    def __init__(self, entryDoor=None, entryDirection=None):
        #self.id = self.generateId()
        self.contents = {}
        if entryDirection != None:
            opposite = self.oppositeDirection(entryDirection)
            self.contents[opposite] = entryDoor
            self.contents[opposite].use()

        for direction in self.directions:
            if not direction in self.contents.keys() and random.random() < self.doorChance:
                self.contents[direction] = Door(self)

        if len(self.contents) < 2:
            self.contents[random.choice(self.directions)] = Door(self)

    def generateId(self):
        out = ''
        for j in range(10):
            out += random.choice(string.ascii_letters)
        return out

    def oppositeDirection(self, direction):
        if direction == 'nord':
            return 'syd'
        elif direction == 'syd':
            return 'nord'
        elif direction == 'vest':
            return 'øst'
        elif direction == 'øst':
            return 'vest'
        elif direction == 'op':
            return 'ned'
        elif direction == 'ned':
            return 'op'

    def __repr__(self):
        out = ''
        #out += self.id
        out += '\n'
        for door in self.contents:
            out += 'Der er en dør mod {}.\n'.format(door)
        return out

class Door():

    def __init__(self, thisRoom, otherRoom=None):
        self.locked = random.choice([True, False])
        self.trapped = random.choice([True, False])
        self.hitpoints = random.randrange(5, 15)
        self.thisRoom = thisRoom
        self.otherRoom = otherRoom

    def use(self):
        self.thisRoom, self.otherRoom = self.otherRoom, self.thisRoom

    def __repr__(self):
        out = 'Du ser en dør'
        if self.locked:
            out += '.\nDen er låst'
        if self.trapped:
            out += ' og ser mistænkelig ud.'
        else:
            out += '.'
        return out

class Chest():

    def __init__(self):
        self.locked = random.choice([True, False])
        self.trapped = random.choice([True, False])
        self.goldContent = random.randrange(1, 100)
