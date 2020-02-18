import QtQuick 2.0
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

ColumnLayout {
    property alias chat: chat
    property alias userlist: userlist
    property alias message: message

    ColumnLayout {
        //anchors.fill: parent

        Text {
            id: chat
            Layout.fillWidth: true
            Layout.fillHeight: true
        }

        Text {
            id: userlist
            width: 150
            Layout.fillHeight: true
        }

        TextField {
            id: message
            height: 50
            Layout.fillWidth: true
            Layout.columnSpan: 2
        }
    }
}
