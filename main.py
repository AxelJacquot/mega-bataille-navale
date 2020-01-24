

class player:
    def __init__(self, name):
        self.name = name
        self.container          = bateau(5, 2)

        self.porte_avion_1      = bateau(5, 1)
        self.porte_avion_2      = bateau(5, 1)

        self.destroyer_1        = bateau(4, 1)
        self.destroyer_2        = bateau(4, 1)
        self.destroyer_3        = bateau(4, 1)

        self.torpilleur_1       = bateau(4, 1)
        self.torpilleur_2       = bateau(4, 1)
        self.torpilleur_3       = bateau(4, 1)

        self.petit_sous_marin_1 = sous_marin(3, 1)
        self.petit_sous_marin_2 = sous_marin(3, 1)
        self.petit_sous_marin_3 = sous_marin(3, 1)
        self.petit_sous_marin_4 = sous_marin(3, 1)
        self.petit_sous_marin_5 = sous_marin(3, 1)

        self.mini_sous_marin    = sous_marin(2, 1)
        self.ss_marin_nucleaire_1 = sous_marin_nucleaire(6, 1)
        self.ss_marin_nucleaire_2 = sous_marin_nucleaire(6, 1)

    def map(self,x,y,layer):
        x = 15
        y = 15
        layer = 3


class bateau :
    def __init__(self, size_x = 0, size_y = 0,pos_x = 0, pos_y = 0, pos_angle = 'H', layer = 1):
        self.angle = pos_angle
        self.size_x = size_x
        self.size_y = size_y
        self.x = pos_x
        self.y = pos_y
        self.layer = layer

    def container(self):


class sous_marin_nucleaire :
    def __init__(self, size_x=0, size_y=0, pos_x=0, pos_y=0,pos_angle = 'H', layer = 2):
        self.angle = pos_angle
        self.size_x = size_x
        self.size_y = size_y
        self.x = pos_x
        self.y = pos_y
        self.layer = layer

class sous_marin :
    def __init__(self, size_x=0, size_y=0, pos_x=0, pos_y=0,pos_angle = 'H', layer = 2):
        self.angle = pos_angle
        self.size_x = size_x
        self.size_y = size_y
        self.x = pos_x
        self.y = pos_y
        self.layer = layer



def place_bateau(player):
    player.container.x      = input("position x du container ?")
    player.container.y      = input("position y du container ?")
    player.container.angle  = input("orientation ?")

    player.porte_avion_1.x  = input("info position x du container")
    player.porte_avion_1.y  = input("info position y du container")

    player.porte_avion_2.x  = input("info position x du container")
    player.porte_avion_2.y  = input("info position y du container")

    player.destroyer_1.x    = input("info position x du container")
    player.destroyer_1.y    = input("info position y du container")
    player.destroyer_2.x        = input("info position x du container")
    player.destroyer_2.y        = input("info position y du container")
    player.destroyer_3.x        = input("info position x du container")
    player.destroyer_3.y        = input("info position y du container")

    player.container.x          = input("info position x du container")
    player.container.y          = input("info position y du container")
    player.ss_marin_nucleaire.x = input("info position x du container")
    player.ss_marin_nucleaire.y = input("info position y du container")
    player.p.x  = input("info position x du container")
    player.ss_marin_nucleaire.y = input("info position y du container")
    player.ss_marin_nucleaire.x = input("info position x du container")
    player.ss_marin_nucleaire.y = input("info position y du container")
    player.ss_marin_nucleaire.x = input("info position x du container")
    player.ss_marin_nucleaire.y = input("info position y du container")

def place_sous_marin():

def config_partie():
    player_1 = player(input("nom joueur"))
    place_bateau(player_1)
def info_player():


