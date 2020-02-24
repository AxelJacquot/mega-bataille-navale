import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3

ColumnLayout{
    Connections{
        target: Client
        onSignalpseudo:{
            console.log("ixi");
            
            main.connect = true
        }
    }
    GridLayout{
        columns: 2
        Text {
            id: textpseudo
            text: qsTr("Pseudo")
        }
        TextField{
            id: pseudo
            placeholderText: "D4RKSaSuKe"
        }
        Text {
            id: textip
            text: qsTr("IP Address ")
        }
        TextField{
            id : ip
            placeholderText: "255.255.255.255"
            validator: RegExpValidator{
                regExp: /(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/
            }
        }
        Text {
            id: textport
            text: qsTr("Game Access Port ")
        }
        TextField{
            id: port
            placeholderText: "00000"
            validator: RegExpValidator{
                regExp: /[0-9]{1,5}/
            }

        }
    }
    RowLayout{
        Button{
            Layout.minimumWidth: 100
            Layout.alignment: Qt.AlignVCenter
            text: qsTr("Connect")
            onClicked: {
                Client.connect(ip.text, port.text, pseudo.text)
            }

        }
    }
}
