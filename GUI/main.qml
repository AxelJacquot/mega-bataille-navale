import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

ApplicationWindow {
    id: main
    visible: true
    width: 640
    height: 480
    title: qsTr("Tabs")

    property bool connect: false
    property bool game: false
    property bool start: false

    PageConnexion{
        visible: !connect

    }

    Game{
        visible: connect
    }

}
