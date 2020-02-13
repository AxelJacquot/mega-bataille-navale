import QtQuick 2.0

import QtQml.Models 2.1
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.5

ColumnLayout {
    width : 200
    //height : 480
    /*ScrollView{
        id: flickable
        width : 200
        height : 480
        //        orientation: Qt.Vertical
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
        ScrollBar.vertical.policy: ScrollBar.AlwaysOn
        ScrollBar.horizontal.interactive: true
        ScrollBar.vertical.interactive: true
        //currentIndex: tabBar.currentIndex
        clip: true*/

        /*Boat{ caseX: 5; caseY: 1; name: "Porte Avion"; nbr: 2; key : "Boat"}
        Boat{ caseX: 5; caseY: 1; name: "Avion"; nbr: 2; key : "Boat"}
        Boat{ caseX: 5; caseY: 1; name: "Porte Avion"; nbr: 2; key : "Boat"}
        Boat{ caseX: 5; caseY: 1; name: "Porte Avion"; nbr: 2; key : "Boat"}
        Boat{ caseX: 5; caseY: 1; name: "Porte Avion"; nbr: 2; key : "Boat"}
        Boat{ caseX: 5; caseY: 1; name: "Porte Avion"; nbr: 2; key : "Boat"}*/

        ListView{
            width : 200
            height : 480
            cacheBuffer: 2000
            model: DelegateModel {
                //! [0]
                id: visualModel
                model: ListModel {
                    id: widtheightModel
                    ListElement { caseX: 5; caseY: 2; name: "Porte Container"; nbr: 1 ; key : "Boat"}
                    ListElement { caseX: 5; caseY: 1; name: "Porte Avion"; nbr: 2 ; key : "Boat"}
                    ListElement { caseX: 4; caseY: 1; name: "Destroyer"; nbr: 3 ; key : "Boat"}
                    ListElement { caseX: 3; caseY: 2; name: "Torpilleur"; nbr: 3 ; key : "Boat"}
                    ListElement { caseX: 6; caseY: 1; name: "Sous-marin Nucléaire"; nbr : 2 ; key : "Boat"}
                    ListElement { caseX: 3; caseY: 1; name: "Petit Sous-marin"; nbr : 5 ; key : "Boat"}
                    ListElement { caseX: 2; caseY: 1; name: "Mini Sous-marin"; nbr : 2; key : "Boat"}
                }
                Boat{}
            }
        }

    //}
}



