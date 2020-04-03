import QtQuick 2.9
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3

ColumnLayout {
    width: main.width
    height: main.height
    spacing: 20
    Layout.margins: 5

    Text {
        id: title
        Layout.alignment: Qt.AlignCenter
        text: qsTr("Règles du jeu")
        font.pointSize: 24
    }

    Text {
        id: regle
        font.pointSize: 8
        Layout.alignment: Qt.AlignCenter
        text: qsTr("        Pour pouvoir jouer à ce jeu, veuillez à ce que les deux joueur soit connéecter au même réseau local.\n
        Pour débuter le jeu, un des joueurs doit se mettre comme hôte de la partie est rentré l'adresse IP qui lui est dédié ainsi qu'un port de communication libre.\n
        Le seconde joueur devra quant à lui, se connecter en Join et rentrer l'adresse IP et le port de l'hôte.\n
        Les deux joueurs doivent se munir d'un pseudo pour commencer la partie.\n\n
        Une fois, que les deux joueurs se sont rejoient. Ils doivent placer tous les bateaux sur la carte.\n
        La carte se séparent en trois niveaux: le premier est pour tout les types de bateaux et sous-marins et les deux dernier niveaux restant sont uniquement pour les sous marins.\n
        Dès que tous les bateaux et sous marins sont placés sur la carte vous pouvez commencer la partie.\n
        Les bateaux et sous marins se trouvent dans un menu déroulant donc il fout suffit jouer avec la roulette de votre souris lorsque vous êtes au dessus.\n
        Pour placer les bateaux et sous marins, il suffit de les prendre de double-cliquer et maintenir le clique gauche de la souris et l'amener sur votre carte et de le lacher à l'endroit où vous souhaitez le mettre\n
        \n
        Il 'sagit d'un jeu au tour par tour, le premier joueur à jouer est l'hôte.\n
        Pour jouer, il suffit de cliquer sur la case sur la carte nous souhaitons tirer.\n
        La partie se termine une fois que tous les bateaux et sous marins d'un joueur sont coulés.")   
    }

     Text {
        id: regle2
        font.pointSize: 7
        Layout.alignment: Qt.AlignCenter
        text: qsTr("        Si problème désactiver les pare-feu et vérifier que les ports soit ouverts.")
    }

    Button{
        text: "Retour"
        Layout.alignment: Qt.AlignCenter
        onClicked: {
            conReg.reg = false
        }
    }
}
