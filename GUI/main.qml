import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("Tabs")

    GridLayout{
        rows: 1
        columns: 3
        anchors.fill: parent
        anchors.margins: 10
        Layout.margins: 30

        MenuBoat{}

        OurSide{}

        EnnemiSide{}
    }
}
