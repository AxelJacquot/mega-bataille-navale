import QtQuick 2.14
import QtQuick.Window 2.2
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.0

Popup {
    x: main.width / 2 + 200
    y: main.height / 2 + 200
    width: 400
    height: 50
    modal: true
    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent
    
    property string message
    ColumnLayout{
        Text {
            wrapMode: Text.Wrap
            text : message
            font.pixelSize: 18
        }
    }
    
            
}
