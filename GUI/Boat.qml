import QtQuick 2.9
import QtQuick.Layouts 1.3

ColumnLayout {
    /*property int caseX
    property int caseY
    property int nbr
    property string name
    property string key*/
    width : 25 * caseX + myText.paintedWidth
    height : 25 * caseX + myText.paintedWidth
    Rectangle {
        width: myText.paintedWidth
        height: myText.paintedHeight

        Text {
            anchors.fill:parent
            id: myText
            font.family: "Helvetica"
            font.pointSize: 18
            text:  qsTr(name)
        }
    }
    GridLayout{
        columns: nbr
        Repeater{
        model: nbr
        Item {
            id: boot
            property bool sens: false
            property bool drop: true
            property bool test: true
            property int mul: caseX * caseY

            width: sens ? 25 * caseX : 25 * caseY
            //height: sens ? 25 * caseY : 25 * caseX

            MouseArea {
                id: mouseArea

                width: sens ? 25 * caseX : 25 * caseY
                height: sens ? 25 * caseY : 25 * caseX
                //anchors.centerIn: parent
                acceptedButtons: Qt.LeftButton | Qt.RightButton
                drag.target: tile
                propagateComposedEvents: true
                pressAndHoldInterval: 60

                onClicked: {
                    if(mouse.button === Qt.LeftButton){
                        drop = false
                        root.typeBoat = typeBoat
                        root.indexBoat = index
                        root.orientation = sens
                    }
                }

                onReleased: {
                    if(mouse.button === Qt.RightButton & drop == false){
                        sens = !sens
                    }
                    if(mouse.button === Qt.LeftButton & drop == false){
                        drop = true
                        
                        //parent = tile.Drag.target
                        root.typeBoat = typeBoat
                        root.indexBoat = index
                        root.orientation = sens
                        if(root.dropAccept == true){
                            parent = tile.Drag.target !== null ? tile.Drag.target : boot
                            tile.Drag.drop()
                        }
                    }
                }

                GridLayout{

                    id : tile

                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    columns: sens ? caseX : caseY
                    rows : sens ? caseY : caseX
                    columnSpacing: 0
                    rowSpacing: 0
                    Drag.keys: [ key ]
                    Drag.active: mouseArea.drag.active
                    Drag.hotSpot.x: 16
                    Drag.hotSpot.y: 16
                    Drag.source: boot
                    Repeater{
                        model: mul
                        ColumnLayout{
                            id: cl
                            /*MouseArea{
                                id: mouseTest
                                width: sens ? 25 * caseX : 25 * caseY
                                height: sens ? 25 * caseY : 25 * caseX

                                drag.target: tile
                                acceptedButtons: Qt.LeftButton
                                onReleased:{
                                    parent = rectBoat.Drag.target !== null ? rectBoat.Drag.target : tile
                                    root.xBoat = sens ? heightMul : widthMul
                                    root.yBoat = sens ? widthMul : heightMul
                                    root.nameBo = boatName
                                    rectBoat.Drag.drop()
                                }
                            }*/
                            Rectangle{
                                id: rectBoat
                                width: 25
                                height: 25
                                //Layout.verticalCenter: parent.verticalCenter
                                //Layout.horizontalCenter: parent.horizontalCenter
                                /*Drag.keys: [ key ]
                                Drag.active: mouseTest.drag.active
                                Drag.hotSpot.x: 16
                                Drag.hotSpot.y: 16
                                Drag.source: boot*/
                                //anchors.fill: parent
                                color: "blue"


                            }
                        }
                    }
                }
                states: State {
                    when: mouseArea.drag.active
                    ParentChange { target: tile; parent: boot }
                    AnchorChanges { target: tile; anchors.verticalCenter: undefined; anchors.horizontalCenter: undefined }
                }


            }
        }
    }
    }
    



}

