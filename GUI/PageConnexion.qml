import QtQuick 2.9
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3

ColumnLayout{
    width: main.width
    height: main.height
    spacing: 20
    Layout.margins: 5

    Text {
        id: title
        text: qsTr("Connexion")
        font.pointSize: 18
        Layout.alignment: Qt.AlignCenter
    }
       
    SwipeView {
        clip: true
        Layout.alignment: Qt.AlignCenter
        currentIndex: bar.currentIndex
        Join{}
        Host{}
    }

    Button {
        Layout.alignment: Qt.AlignCenter
        text: qsTr("Règles")
        onClicked: {
            conReg.reg = true
        }
    }
    
    TabBar{
        id: bar
        Layout.alignment: Qt.AlignCenter
        TabButton{
            width: 100
            text: qsTr("Rejoindre")
        }
        TabButton{
            width: 100
            text: qsTr("Hôte")
        }
    }
}
