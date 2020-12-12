from debug import *
from ennemy import *

class Player:

    def __init__(self, name : str, hp : float, atk : float, dfc : float, debug = False):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfc = dfc
        self.dead = False
        debug_print(debug, name + " Player stats succesfully created")

    def check_alive(self, name):
        if self.hp <= 0:
            self.dead = True
            print(self.name + " has been killed by " + name)

    def attack(self, ennemy : Ennemy, debug = False):
        ennemy.get_attacked(self.name, self.atk)
        debug_print(debug, "Ennemy attacked with " + str(self.atk) + " atk point")

    def defence(self, debug = False):
        pass

    def magic(self, debug = False):
        pass

    def inventory(self, debug = False):
        pass

    def get_atacked(self, name, atk):
        self.hp -= min_int_0(atk-self.dfc)
        print(self.name+" is Attacked by "+name+" and deal "+str(min_int_0(atk-self.dfc))+" damage")
        self.check_alive(name)
