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
       
    SwipeView{
        clip: true
        Layout.alignment: Qt.AlignCenter
        currentIndex: bar.currentIndex
        Join{}
        Host{}
    }
    
    TabBar{
        id: bar
        Layout.alignment: Qt.AlignCenter
        TabButton{
            text: qsTr("Join")
        }
        TabButton{
            text: qsTr("Host")
        }
    }
}
