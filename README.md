# mega-bataille-navale  [![Build Status](https://travis-ci.com/AxelJacquot/mega-bataille-navale.svg?branch=master)](https://travis-ci.com/AxelJacquot/mega-bataille-navale) [![Coverage Status](https://coveralls.io/repos/github/AxelJacquot/mega-bataille-navale/badge.svg?branch=master)](https://coveralls.io/github/AxelJacquot/mega-bataille-navale?branch=master)

Projet d'école de méga bataille navale



# Etape 0 : Clonner le Projet
git clone https://github.com/AxelJacquot/mega-bataille-navale.git


# Etape 1 : Création de l'envirronnement virtuel
aller dans le dossier cloner

python3.8 -m venv venv
source venv/bin/activate

# Etape 2 : Installez les dépendances
pip install -r requirements.txt

# Etape 3 : Lancement du projet


python main.py

Pour que le jeu fonctionne les deux personne doivent être sur le même reseaux.
Un des deux joueur doit être l'hôtes et mettre un pseudo son adresse Ip et mettre le port 5454
l'autres joueur doit mettre son pseudo , l'adresse ip de l'hôtes le même port 5454

L'interface ne ce lance pas tant que les deux joueurs ne sont pas présent. 
La partie ne se lance que si les deux personne ont placé leurs bateaux

