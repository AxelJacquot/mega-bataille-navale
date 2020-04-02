import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

ApplicationWindow {
    id: main
    visible: true
    width: 1080
    height: 570
    minimumHeight: height
    minimumWidth: width
    maximumHeight: height
    maximumWidth: width
    title: qsTr("BattleShip")

    property bool connect: false
    property bool game: false
    property bool start: false
    property string ourPseudo
    property string ennemyPseudo
    property bool havePseudo: false
    property int ourBoatDefeat : 0
    property int ennemyBoatDefeat: 0

    ConReg{
        visible: connect
    }

    Game{
        visible: !connect
    }

}
