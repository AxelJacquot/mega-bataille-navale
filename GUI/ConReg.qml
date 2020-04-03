import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Item {
    id: conReg
    width: main.width
    height: main.height

    property bool reg: false

    PageConnexion{
        visible: !reg
    }

    Regle{
        visible: reg
    }

}
