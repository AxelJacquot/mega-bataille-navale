

class player:
    def __init__(self):
        self.name = ""
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

        self.mini_sous_marin_1  = sous_marin(2, 1)
        self.mini_sous_marin_2  = sous_marin(2, 1)
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
        pass


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

    player.porte_avion_1.x      = input("position x du port-avion ?")
    player.porte_avion_1.y      = input("position y du port-avion ?")
    player.porte_avion_1.angle  = input("orientation ?")


    player.porte_avion_2.x      = input("position x du port-avion ?")
    player.porte_avion_2.y      = input("position y du container ?")
    player.porte_avion_2.angle  = input("orientation ?")

    player.destroyer_1.x      = input("position x du destroyer ?")
    player.destroyer_1.y      = input("position y du destroyer ?")
    player.destroyer_1.angle  = input("orientation ?")

    player.destroyer_2.x      = input("position x du destroyer ?")
    player.destroyer_2.y      = input("position y du destroyer ?")
    player.destroyer_2.angle  = input("orientation ?")

    player.destroyer_3.x = input("position x du destroyer ?")
    player.destroyer_3.y = input("position y du destroyer ?")
    player.destroyer_3.angle = input("orientation ?")

    player.torpilleur_1.x = input("position x du torpilleur ?")
    player.torpilleur_1.y = input("position y du torpilleur ?")
    player.torpilleur_1.angle = input("orientation ?")

    player.torpilleur_2.x = input("position x du torpilleur ?")
    player.torpilleur_2.y = input("position y du torpilleur ?")
    player.torpilleur_2.angle = input("orientation ?")

    player.torpilleur_3.x = input("position x du torpilleur ?")
    player.torpilleur_3.y = input("position y du torpilleur ?")
    player.torpilleur_3.angle = input("orientation ?")


def place_sous_marin(player):
    player.ss_marin_nucleaire_1.x = input("position x du sous-marin-nucleaire ?")
    player.ss_marin_nucleaire_1.y = input("position y du sous-marin-nucleaire ?")
    player.ss_marin_nucleaire_1.angle = input("orientation ?")

    player.ss_marin_nucleaire_2.x = input("position x du sous-marin-nucleaire ?")
    player.ss_marin_nucleaire_2.y = input("position y du sous-marin-nucleaire ?")
    player.ss_marin_nucleaire_2.angle = input("orientation ?")

    player.petit_sous_marin_1.x = input("position x du petit sous-marin ?")
    player.petit_sous_marin_1.y = input("position y du petit sous-marin ?")
    player.petit_sous_marin_1.angle = input("orientation ?")

    player.petit_sous_marin_2.x = input("position x du petit sous-marin ?")
    player.petit_sous_marin_2.y = input("position y du petit sous-marin ?")
    player.petit_sous_marin_2.angle = input("orientation ?")

    player.petit_sous_marin_3.x = input("position x du petit sous-marin ?")
    player.petit_sous_marin_3.y = input("position y du petit sous-marin ?")
    player.petit_sous_marin_3.angle = input("orientation ?")

    player.petit_sous_marin_4.x = input("position x du petit sous-marin ?")
    player.petit_sous_marin_4.y = input("position y du petit sous-marin ?")
    player.petit_sous_marin_4.angle = input("orientation ?")

    player.petit_sous_marin_5.x = input("position x du petit sous-marin ?")
    player.petit_sous_marin_5.y = input("position y du petit sous-marin ?")
    player.petit_sous_marin_5.angle = input("orientation ?")

    player.mini_sous_marin_1.x = input("position x du petit sous-marin ?")
    player.mini_sous_marin_1.y = input("position y du petit sous-marin ?")
    player.mini_sous_marin_1.angle = input("orientation ?")

    player.mini_sous_marin_2.x = input("position x du mini sous-marin ?")
    player.mini_sous_marin_2.y = input("position y du mini sous-marin ?")
    player.mini_sous_marin_2.angle = input("orientation ?")

def config_partie(player):
    player.name = input("entrer non joueur: ")
    place_bateau(player)
    place_bateau(player)

def start_partie():
    player_1 = player()
    player_2 = player()
    config_partie(player_1)
    config_partie(player_2)

#if __name__=="main":
start_partie()

