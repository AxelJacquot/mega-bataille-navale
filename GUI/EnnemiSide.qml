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
        verticalPadding: verticalPadding

        TabButton {
            text: qsTr("1")
        }
        TabButton {
            text: qsTr("2")
        }
        TabButton{
            text:  qsTr(("3"))
        }
    }
}


