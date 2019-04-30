import random as r

class Creature():

    def __init__(self, creatureName, hitpoints):
        self.creatureName = creatureName
        self.hitpoints = hitpoints

    def takeDamage(self, amount):
        self.hitpoints -= amount

    def attack(self, anEnemy):
        pass

    def __repr__(self):
        return 'Der er en {} i rummet.'.format(self.creatureName)

class Player(Creature):

    def __init__(self, playerName):
        super().__init__(playerName, 20)

    def __repr__(self):
        width = 60
        out = '|{}|'.format(self.creatureName)
        while len(out) < width:
            out = '-' + out + '-'
        out += '\nHitpoints:\t{}\n'.format(self.hitpoints)
        return out


class Snothvalp(Creature):

    def __init__(self, creatureName):
        super().__init__(creatureName, r.randint(7,12))

    def __repr__(self):
        return 'Der er en snorthvalp ved navn {} i rummet'.format(self.creatureName.title())

# Kode til unit-testing af klasserne i denne fil
if __name__ == '__main__':
    c = Creature('jægersoldat', 1)
    s = Snothvalp('joKum')
    print(c)
    print(s)
