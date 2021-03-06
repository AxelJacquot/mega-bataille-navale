import QtQuick 2.0

import QtQml.Models 2.1
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.5

ColumnLayout {
    id: mBoat
    property bool rec : false
    width : 250
    spacing : 125
    property int boatPlace: 18

    
    
    ColumnLayout{
        width : 250
        height : 400
        ListView{
            Layout.alignment: Qt.AlignTop
            width : 250
            height : 350
            cacheBuffer: 2000
            model: DelegateModel {
                //! [0]
                id: visualModel
                model: ListModel {
                    id: widtheightModel
                    ListElement { caseX: 5; caseY: 2; name: "Porte Container"; nbr: 1 ; key : "Boat"; typeBoat: 1}
                    ListElement { caseX: 5; caseY: 1; name: "Porte Avion"; nbr: 2 ; key : "Boat"; typeBoat: 3}
                    ListElement { caseX: 4; caseY: 1; name: "Destroyer"; nbr: 3 ; key : "Boat"; typeBoat: 2}
                    ListElement { caseX: 3; caseY: 2; name: "Torpilleur"; nbr: 3 ; key : "Boat"; typeBoat: 4}
                    ListElement { caseX: 6; caseY: 1; name: "Sous-marin Nucléaire"; nbr : 2 ; key : "Submarine"; typeBoat: 5}
                    ListElement { caseX: 3; caseY: 1; name: "Petit Sous-marin"; nbr : 5 ; key : "Submarine"; typeBoat: 6}
                    ListElement { caseX: 2; caseY: 1; name: "Mini Sous-marin"; nbr : 2; key : "Submarine"; typeBoat: 7}
                }
                Boat{}
            }
        }
    }
    ColumnLayout{
        Rectangle {
            width: test.paintedWidth
            height: test.paintedHeight
            Text {
                anchors.fill:parent
                id: test
                font.family: "Helvetica"
                font.pointSize: 10
                text:  "Bateau Restant :" + boatPlace + "/" + "18"
            }
        }
        Button{
            Layout.minimumWidth : 100
            Layout.alignment: Qt.AlignVCenter
            text: qsTr("Lancer la partie")
            onClicked: {
                if (boatPlace == 0) {
                    console.log("Lancer")
                    Reseau.sendPseudo(1, main.ourPseudo)
                    main.start = true
                }   
            }
        }
    }
}



