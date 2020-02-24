import QtQuick 2.9
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3

ColumnLayout{
    spacing: 20
    Layout.margins: 5
    Connections{
       // target:

    }

    Text {
        id: title
        text: qsTr("Connexion")
        font.pointSize: 18
        Layout.alignment: Qt.AlignCenter
    }
    StackLayout{
        currentIndex: bar.currentIndex
        Join{}
        Host{}
    }

    TabBar{
        id: bar
        Layout.alignment: Qt.AlignBottom
        TabButton{
            text: qsTr("Join")
        }
        TabButton{
            text: qsTr("Host")
        }
    }
}
