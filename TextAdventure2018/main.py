# Dette er et lille og simpelt uendeligt teksteventyr til en øvelse i git

import random

from world import World, Door
from creatures import Player

class Game():

    def __init__(self, aPlayer):
        self.thePlayer = aPlayer
        self.theWorld = World()

    def runGame(self):
        while True:
            print(self.thePlayer)
            print(self.theWorld.currentRoom)
            ind = input('Hvad vil du gøre?\n').lower()
            action = self.getAction(ind)
            target = self.getTarget(ind)

            if action == 'gå' and target in self.theWorld.currentRoom.directions:
                self.enterDoor(target)
            elif action == 'se' and target in self.theWorld.currentRoom.contents.keys():
                print(self.theWorld.currentRoom.contents[target])
            else:
                print('Det kan ikke lade sig gøre!')

    def enterDoor(self, direction):
        if self.theWorld.currentRoom.contents[direction].locked:
            print('Døren er låst.\n')
        else:
            print('\nDu går gennem døren mod {}.'.format(direction))
            if self.theWorld.currentRoom.contents[direction].trapped:
                self.springTrap()
            otherroom = self.theWorld.currentRoom.contents[direction].otherRoom
            if otherroom != None:
                self.theWorld.currentRoom.contents[direction].use()
                self.theWorld.currentRoom = otherroom
            else:
                self.theWorld.newRoom(direction)
                self.theWorld.currentRoom.contents[self.theWorld.currentRoom.oppositeDirection(direction)].use()

    def springTrap(self):
        damage = random.randint(1, 10)
        print('Du gik i en fælde og tog {} skade. AV!'.format(damage))
        self.thePlayer.takeDamage(damage)

    def getAction(self, ind):
        # Gå igennem en ulåst dør
        if 'gå' in ind or 'løb' in ind:
            return 'gå'
        # Angrib en dør, en kiste eller et væsen i rummet
        elif 'angrib' in ind or 'nak' in ind:
            pass
        # Dirk en låst dør op... hvis du kan
        elif 'dirk' in ind:
            pass
        # Undersøg en dør, en kiste eller et væsen i rummet
        elif 'undersøg' in ind or 'se' in ind:
            return 'se'
        # Uskadeliggør en fælde på en dør eller en kiste
        elif 'afmonter':
            pass

    def getTarget(self, ind):
        for target in self.theWorld.currentRoom.contents:
            if target in ind:
                return target

if __name__ == '__main__':
    # Sej overskrift genereret med http://www.patorjk.com/software/taag
    # Teksteffeter for ekstra retro-effekt med ANSI koder (http://ozzmaker.com/add-colour-to-text-in-python/)
    print("""
            Det uendelige...\033[1;32;40m \n
    ▄▄▄█████▓▓█████  ██ ▄█▀  ██████ ▄▄▄█████▓▓█████ ██▒   █▓▓█████  ███▄    █ ▄▄▄█████▓▓██   ██▓ ██▀███
    ▓  ██▒ ▓▒▓█   ▀  ██▄█▒ ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀▓██░   █▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒ ▒██  ██▒▓██ ▒ ██▒
    ▒ ▓██░ ▒░▒███   ▓███▄░ ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██  █▒░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░  ▒██ ██░▓██ ░▄█ ▒
    ░ ▓██▓ ░ ▒▓█  ▄ ▓██ █▄   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░   ░ ▐██▓░▒██▀▀█▄
      ▒██▒ ░ ░▒████▒▒██▒ █▄▒██████▒▒  ▒██▒ ░ ░▒████▒  ▒▀█░  ░▒████▒▒██░   ▓██░  ▒██▒ ░   ░ ██▒▓░░██▓ ▒██▒
      ▒ ░░   ░░ ▒░ ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░  ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░      ██▒▒▒ ░ ▒▓ ░▒▓░
        ░     ░ ░  ░░ ░▒ ▒░░ ░▒  ░ ░    ░     ░ ░  ░  ░ ░░   ░ ░  ░░ ░░   ░ ▒░    ░     ▓██ ░▒░   ░▒ ░ ▒░
      ░         ░   ░ ░░ ░ ░  ░  ░    ░         ░       ░░     ░      ░   ░ ░   ░       ▒ ▒ ░░    ░░   ░
                ░  ░░  ░         ░              ░  ░     ░     ░  ░         ░           ░ ░        ░
                                                        ░                               ░ ░
            \033[1;37;40mEn endeløs famlen i mørket!\n\n\n
    """)

    playerName = input('Velkommen fremmede. Hvad er dit navn\n')
    theGame = Game(Player(playerName.title()))
    print('Held og lykke på din færd {}!\n\n'.format(theGame.thePlayer.creatureName))

    theGame.runGame()
