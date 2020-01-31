
class sous_marin:
    def __init__(self, size_x=0, size_y=0, pos_x=0, pos_y=0, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.x = pos_x
        self.y = pos_y
        self.layer = layer




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
