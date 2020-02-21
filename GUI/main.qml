import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

ApplicationWindow {
    id : root
    visible: true
    width: 640
    height: 480
    title: qsTr("Tabs")
    property int typeBoat: 0
    property int indexBoat: 0
    property bool orientation: false

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
