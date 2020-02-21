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
    property int indexLayer: viewOur.currentIndex
    Repeater {
        model: 225
        ColumnLayout{
            id: cl
            property bool boat: false
            property int posX
            property int posY
            property int i
            DropArea{
                id : dragTarget
                width: 25
                height: 25
                keys: placekey
                onDropped: {
                    //drag.accepted = false
                    i = index
                    posX = i /15
                    posY = i % 15
                    console.log(posX)
                    console.log(posY)
                    console.log(indexLayer)
                    console.log(root.typeBoat)
                    console.log(root.indexBoat)
                    console.log(root.orientation)
                    Player.PSM(posX, posY, indexLayer, root.typeBoat, root.indexBoat, root.orientation)
                }
                Rectangle {
                    id: dropRectangle

                    anchors.fill: parent
                    color: colorkey
                    border.color: Qt.lighter(color)
                    opacity: 0.5
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

            /*Rectangle {

                id : rectOur
                width: 25; height: 25
                color : (boat || mouseA.containsMouse) ? "#54647d" : "dark blue"
                border.color: Qt.lighter(color)
                MouseArea{
                    id: mouseA
                    anchors.fill: parent
                    propagateComposedEvents: true
                    acceptedButtons: Qt.LeftButton | Qt.RightButton
                    cursorShape: Qt.PointingHandCursor
                    onClicked: {
                        if (mouse.button === Qt.RightButton){
                            i = index
                            posX = i /15
                            posY = i % 15
                            console.log(index)
                            console.log(posX)
                            console.log(posY)
                        }
                        else
                            rectOur.color = "Blue"
                    }
                }
            }*/

        }


    }


}
