import QtQuick 2.5
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4

GridLayout{
    id:root
    rows: 15
    columns: 15
    columnSpacing: 0
    rowSpacing: 0
    property int indexFloor: index
    MaPopUp{
        id: popVictory
        message: "Vous avez gagné"
    }
    MaPopUp{
        id: popReplay
        message: "Vous pouvez rejouer"
    }
    Repeater {
        model: 225
        Rectangle {
            id : rectEn
            property int posX: index / 15
            property int posY: index % 15
            width: 25; height: 25
            color: "grey"
            border.color: Qt.lighter(color)
            
            function reponse(x,y,lay, touch, coule){
                if(x == posX && y == posY && lay == indexFloor){
                    console.log("layer reponse: " + lay)
                    console.log("layer index: " + indexFloor)
                    if(touch == true){
                        color = 'red';
                    }
                    else{
                        color = 'blue';
                    }
                    if(coule == true){
                        console.log("coule")
                        main.ennemyBoatDefeat = main.ennemyBoatDefeat + 1
                        if(main.ennemyBoatDefeat == 18){
                            popVictory.open()
                        }
                    }
                }
            }

            Component.onCompleted :{
                Attack.TargetQMl.connect(reponse)
            }
            
            MouseArea{
                anchors.fill: parent
                acceptedButtons: Qt.LeftButton | Qt.RightButton
                cursorShape: Qt.OpenHandCursor
                onDoubleClicked: {
                    if(main.game == true && main.start == true && main.havePseudo == true){
                        
                        var error = Attack.tire(posX, posY)
                        if(error == false){
                            main.game = false;
                        }
                        else{
                            popReplay.open()
                        }
                    }                           
                }
            }
        }
    }
}
