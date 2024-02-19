import serial.tools.list_ports
import serial
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from panelui import Ui_MainWindow

class MySerialApp(QMainWindow): 
    def __init__(self):
        super(MySerialApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        ports = serial.tools.list_ports.comports()
        self.ui.cbCOM.addItems(ports)
        

        self.ui.btnConnect.clicked.connect(self.connect)

    def connect(self):
        port = self.ui.cbCOM.currentText()
        print(f"Conectando a {port}")
        self.ser = serial.Serial(port, 9600)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySerialApp()
    window.show()
    sys.exit(app.exec())