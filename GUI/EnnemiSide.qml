import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12

ColumnLayout{
    StackLayout {
        currentIndex: tabBarEnnemi.currentIndex
        id: viewEnnemi
        Repeater{
            model: 3
            EnemiFloor{}
        }
    }

   TabBar {
        id: tabBarEnnemi
        currentIndex: viewEnnemi.currentIndex
        Layout.alignment: Qt.AlignCenter
        TabButton {
            text: qsTr("Surface")
            width: 90
        }
        TabButton {
            text: qsTr("Peu Profond")
            width: 90
        }
        TabButton{
            text:  qsTr(("Profond"))
            width: 90
        }
    }
}


