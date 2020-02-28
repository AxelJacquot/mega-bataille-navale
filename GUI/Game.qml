import QtQuick 2.0
import QtQuick.Layouts 1.3

GridLayout{
    id : root
    rows: 1
    columns: 3
    anchors.fill: parent
    anchors.margins: 10
    Layout.margins: 30
        
    property int typeBoat: 0
    property int indexBoat: 0
    property bool orientation: false
    property bool dropAccept : false
    property bool dropEffect: false

    property int ourBoatSunk: 0             //count boat to victory or defeat
    property int ennemiBoatSunk: 0          //count boat to victory or defeat

    MaPopUp{
        id: popStart
        message: "La partie peut commencer"
    }

    function ennemyPseudo(pseudo) {
        main.ennemyPseudo = pseudo
        main.havePseudo = true
        popStart.open()
    }
    Component.onCompleted : {
        Reseau.playerConnected.connect(ennemyPseudo)
    }
    MenuBoat{}

    OurSide{}

    EnnemiSide{}
}
