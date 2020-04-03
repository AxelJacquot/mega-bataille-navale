import QtQuick 2.9
import QtQuick.Layouts 1.3

ColumnLayout {
    width : 25 * caseX + myText.paintedWidth + test.paintedWidth + 10
    height : 25 * caseX + myText.paintedHeight + test.paintedHeight +10
    spacing: 5
    property int nbrBoat: nbr
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
    Rectangle {
        width: test.paintedWidth
        height: test.paintedHeight
        Text {
            anchors.fill:parent
            id: test
            font.family: "Helvetica"
            font.pointSize: 10
            text:  "Bateau placer :" + nbrBoat + "/" + nbr
        }
    }
    GridLayout{
        columns: nbr
        Repeater{
            model: nbr
            Item {
                id: boot
                property bool sens: false
                property bool drop: false
                property bool test: true
                property int mul: caseX * caseY
                property bool opac: false
                width: sens ? 25 * caseY : 25 * caseY
                height: sens ? 25 * caseX : 25 * caseX
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
                            /*if(root.dropEffect == false){
                                drop = false
                            }*/
                            
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
                            //parent = tile.Drag.target
                            root.typeBoat = typeBoat
                            root.indexBoat = index
                            root.orientation = sens
                            if(root.dropAccept == true){
                                parent = tile.Drag.target !== null ? tile.Drag.target : boot
                                tile.Drag.drop()
                                if(root.dropEffect == true){
                                    nbrBoat = nbrBoat - 1
                                    mBoat.boatPlace = mBoat.boatPlace - 1
                                    opac = true
                                    drop = true
                                    root.dropEffect = false
                                }
                                
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
                                Rectangle{
                                    id: rectBoat
                                    width: 25
                                    height: 25
                                    color: "blue"
                                    opacity: index == 0 && opac ? 0.65 : 1
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
