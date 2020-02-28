import QtQuick 2.5
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

GridLayout{
    id: gridLayoutOur
    rows: 15
    columns: 15
    columnSpacing: 0
    rowSpacing: 0
    property string placekey
    property string colorkey
    property int indexFloor
    property var key : [placekey, "Submarine"]
    Repeater {
        model: 225
        ColumnLayout{
            id: cl
            property bool boat: false
            property int posX : index / 15
            property int posY : index % 15
            DropArea{
                id : dragTarget
                width: 25
                height: 25
                keys: key
                onEntered: {
                    console.log("Test")
                    var error = Player.TestPlaceBoat(posX, posY, root.typeBoat, root.indexBoat, root.orientation)
                    if(error == false){
                        console.log(error)
                        root.dropAccept = false
                    }
                    else{
                        root.dropAccept = true
                    }
                }

                onDropped: {
                    //drag.accepted = false
                    var error = Player.PlaceBoat(posX, posY, indexFloor, root.typeBoat, root.indexBoat, root.orientation)
                    console.log(error)
                    if(error == false){
                        drop.accept(Qt.IgnoreAction)
                    }
                    else{
                        drop.accept()
                    }
                }
                Rectangle {
                    id: dropRectangle

                    anchors.fill: parent
                    color: colorkey
                    border.color: Qt.lighter(color)
                    opacity: 0.5
                    Component.onCompleted : {
                        Defense.ShootQML.connect(reponse)
                    }

                    function reponse(x, y, lay, touche){
                        if(x == posX && y == posY && lay == indexFloor){
                            console.log(lay)
                            console.log(indexFloor)
                            if(touche == 1){
                                color = 'black'
                            }  
                        }
                        main.game = true
                    }
                    
                    //visible: parent.containsDrag

                    states: [
                        State {
                            when: dragTarget.containsDrag

                            PropertyChanges {
                                target: dropRectangle
                                color: "grey"

                            }
                        }
                    ]

                }

            }
        }
    }
}
