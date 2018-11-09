class Creature():

    def __init__(self, creatureName, hitpoints):
        self.creatureName = creatureName
        self.hitpoints = hitpoints

    def takeDamage(self, amount):
        pass

    def attack(self, anEnemy):
        pass

class Player(Creature):

    def __init__(self, playerName):
        super().__init__(playerName, 20)

    def __repr__(self):
        out = ''
        out += '-------|{}|--------\n'.format(self.creatureName)
        out += 'Hitpoints:\t{}\n'.format(self.hitpoints)
        return out
