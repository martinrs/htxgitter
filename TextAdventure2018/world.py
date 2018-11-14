import random
import string

class World():

    def __init__(self):
        self.currentRoom = Room()

    def newRoom(self, entryDirection):
        new = Room(self.currentRoom.contents[entryDirection], entryDirection)
        new.contents[new.oppositeDirection(entryDirection)].otherRoom = self.currentRoom
        self.currentRoom.contents[entryDirection].otherRoom = new
        self.currentRoom = new

class Room():

    doorChance = 0.5
    directions = ['nord', 'syd', 'øst', 'vest', 'op', 'ned']

    def __init__(self, entryDoor=None, entryDirection=None):
        self.id = self.generateId()
        self.mood = random.choice(self.importList('stemningsord.txt'))
        self.color = random.choice(self.importList('farver.txt'))

        self.contents = {}
        if entryDirection != None:
            opposite = self.oppositeDirection(entryDirection)
            entryDoor.otherRoom = self
            self.contents[opposite] = entryDoor

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

    def importList(self, file):
        # Kendt bug: Skærer et bogstav af sidste linie i filen.
        # Kan hackes ved at indsætte tom linie sidst i filen.
        file = open(file, 'r', encoding="utf-8")
        list = []
        for line in file:
            list.append(line.strip().lower())
        file.close()
        return list

    def __repr__(self):
        out = 'Du er i et rum med vægge i en {} {} farve.'.format(self.mood, self.color)
        #out = self.id
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
        out = 'Du ser er en '
        if self.locked:
            out += 'låst '
        if self.locked and self.trapped:
            out += 'og '
        if self.trapped:
            out += 'mistænkeligt udseende '
        out += 'dør.\n'
        #out += 'Døren fører fra {} til {}'.format(self.thisRoom.id, self.otherRoom.id)
        return out

class Chest():

    def __init__(self):
        self.locked = random.choice([True, False])
        self.trapped = random.choice([True, False])
        self.goldContent = random.randrange(1, 100)
