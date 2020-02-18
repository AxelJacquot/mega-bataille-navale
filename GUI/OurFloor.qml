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
                    console.log(drag.x)
                    console.log(drag.y)
                    //drag.accepted = false
                    i = index
                    posX = i /15
                    posY = i % 15
                    console.log(index)
                    console.log(posX)
                    console.log(posY)
                    /*console.log(root.xBoat)
                    console.log(root.yBoat)
                    console.log(root.nameBo)*/
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
