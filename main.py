from debug import *
from player import *
from ennemy import *
from random import *

players = [Player(name = "ToufouMaster", hp = 5, atk = 2, dfc = 0, debug = True)]
ennemies = []

def respawn_ennemies():
    global ennemies
    ennemies = [Ennemy("Mob", randint(1,3), uniform(1,1.5), uniform(0.1,1), True)]

def fight_choice():
    choice = None
    while type(choice) is not int:
        choice = input("Attaque: 0, Defendre: 1, Magie: 2, Inventaire: 3; ")

        try:
           choice = int(choice)
        except:
            print("Attention le choix n'est pas correct!")

        if type(choice) is int:
            if choice >= 0 and choice <= 3:
                if choice == 0: #Attack
                    players[0].attack(ennemies[0])
                elif choice == 1: #Defence
                    players[0].defence()
                elif choice == 2: #Magic
                    players[0].magic()
                elif choice == 3: #Inventory
                    players[0].inventory()
            else:
                print("Attention nombre trop élevé ou trop bas!")
    

def main():
    while True:
        #Verifier si les ennemies sont morts si oui faire apparaitre de Nouveaux
        alldead = True
        for e in ennemies:
            if not e.dead:
                alldead = False
                break
        if alldead or len(ennemies) == 0:
            respawn_ennemies()
                
                
                
        #Faire un Choix entre utiliser des items attacker defendre utiliser la magie et autre
        for p in players:
            if not p.dead:
                #TODO: Integrer un systeme de choix de personnage et de monstre a attaquer
                fight_choice()

        for e in ennemies:
            if not e.dead:
                e.attack(players)

        palldead = True
        for p in players:
            if not p.dead:
                palldead = False
                break
        
        if palldead or len(players) == 0:
            print("All heroes are dead Game Over!")
            break
        

main()
