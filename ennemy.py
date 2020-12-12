from debug import *
from random import *

class Ennemy:

    def __init__(self, name : str, hp : float, atk : float, dfc : float, debug = False):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfc = dfc
        self.dead = False
        debug_print(debug, name + " Ennemy stats succesfully created")

    def check_alive(self, name):
        if self.hp <= 0:
            self.dead = True
            print(self.name + " has been killed by " + name)

    def attack(self, players, debug = False):
        #TODO: Creer un algorythme de priorité d'attaque
        atkedplayer = randint(0, len(players)-1)
        if not players[atkedplayer].dead:
            players[atkedplayer].get_atacked(self.name, self.atk)
        debug_print(debug, "Player attacked with " + str(self.atk) + " atk point")
        

    def defence(self, debug = False):
        pass

    def magic(self, debug = False):
        pass

    def get_attacked(self, name, atk):
        self.hp -= min_int_0(atk-self.dfc)
        print(self.name+" is Attacked by "+name+" and deal "+str(min_int_0(atk-self.dfc))+" damage")
        self.check_alive(name)
