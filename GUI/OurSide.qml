import QtQuick 2.12
import QtQml.Models 2.1
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12

ColumnLayout{
    StackLayout {
        id: viewOur
        currentIndex: tabBarOur.currentIndex //index par défaut
        //orientation: Qt.Vertical
        OurFloor{placekey : "Boat"; colorkey: "cornflowerblue"; indexFloor: 0}
        OurFloor{placekey : "Submarine"; colorkey: "darkslateblue"; indexFloor: 1}
        OurFloor{placekey : "Submarine"; colorkey : "midnightblue"; indexFloor: 2}
    }

    TabBar {
         id: tabBarOur
         currentIndex: viewOur.currentIndex
         TabButton {
             text: qsTr("1")
         }
         TabButton {
             text: qsTr("2")
         }
         TabButton{
             text:  qsTr("3")
         }
     }
}


