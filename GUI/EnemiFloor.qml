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

    Repeater {
        model: 225
        Rectangle {
            id : rectEn
            width: 25; height: 25
            color: "grey"
            border.color: Qt.lighter(color)
            MouseArea{
                anchors.fill: parent
                acceptedButtons: Qt.LeftButton | Qt.RightButton
                cursorShape: Qt.OpenHandCursor
                onClicked: {
                    if (mouse.button === Qt.RightButton)
                        rectEn.color = 'blue';
                    else
                        rectEn.color = 'red';
                }
            }
        }
    }
}
