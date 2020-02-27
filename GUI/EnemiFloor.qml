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
    property int indexFloor: viewEnnemi.currentIndex
    Repeater {
        model: 225
        Rectangle {
            id : rectEn
            property int posX: index / 15
            property int posY: index % 15
            width: 25; height: 25
            color: "grey"
            border.color: Qt.lighter(color)
            
            function reponse(x,y,lay, touch){
                if(x == posX && y == posY && lay == indexFloor){
                    console.log("coule")
                    if(touch == true){
                        color = 'blue';
                    }
                    else{
                        color = 'red';
                    }
                    for(int = 0; i < 100; i++);
                    Reseau.receiveData()
                }
            }

            Component.onCompleted :{
                Attack.TargetQMl.connect(reponse)
            }
            
            MouseArea{
                anchors.fill: parent
                acceptedButtons: Qt.LeftButton | Qt.RightButton
                cursorShape: Qt.OpenHandCursor
                onClicked: {
                    if(main.game = true && main.start == true){
                        console.log(posX)
                        console.log(posY)
                        console.log(indexFloor)
                        Attack.tire(posX, posY) 
                    }                           
                }
            }
        }
    }
}
