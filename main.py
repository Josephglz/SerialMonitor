import serial.tools.list_ports
import serial
import sys
import time
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow
from SerialMonitor.panelui import Ui_MainWindow

class SerialReader(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, ardCom):
        super().__init__()
        self.ardCom = ardCom
        self.running = True

    def run(self):
        while self.running:
            if self.ardCom and self.ardCom.isOpen():
                try:
                    line = self.ardCom.readline().decode("utf-8").strip()
                    if line:
                        self.message_received.emit(line)
                except serial.SerialException as e:
                    print(f"Error al leer del puerto: {e}")
                time.sleep(0.1)

    def stop(self):
        self.running = False

class MySerialApp(QMainWindow): 
    ardCom = None
    
    def __init__(self):
        super(MySerialApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnConnect.clicked.connect(self.connect)
        self.ui.btnDisconnect.clicked.connect(self.disconnect)
        self.ui.btnSend.clicked.connect(self.send)
        self.ui.btnUpdate.clicked.connect(self.scan_serial_ports)
        self.scan_serial_ports()

        self.serial_reader = None

    def scan_serial_ports(self):
        self.ui.cbCOM.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.cbCOM.addItem(port.device)

    def connect(self):
        self.ui.txtSerial.clear()
        port = self.ui.cbCOM.currentText()
        baudrate = self.ui.cbBaudrate.currentText()
        self.ui.txtSerial.append(f"Conectando a {port} con velocidad: {baudrate}")
        try:
            self.ardCom = serial.Serial(port, baudrate)
            if self.ardCom.isOpen():
                self.ui.txtSerial.append(f"Conexión establecida!")
                self.ui.btnConnect.setEnabled(False)
                self.ui.cbCOM.setEnabled(False)
                self.ui.cbBaudrate.setEnabled(False)
                self.ui.btnUpdate.setEnabled(False)
                self.ui.btnDisconnect.setEnabled(True)
                self.ui.btnSend.setEnabled(True)
                self.ui.txtMessage.setReadOnly(False)
                self.start_serial_reader()
            else:
                self.ui.txtSerial.append(f"No se pudo abrir la conexión al puerto {port}.")
        except serial.SerialException as e:
            self.ui.txtSerial.append(f"Error al conectar al puerto {port}: {e}")

    def start_serial_reader(self):
        self.serial_reader = SerialReader(self.ardCom)
        self.serial_reader.message_received.connect(self.update_textbox)
        self.serial_reader.start()

    def disconnect(self):
        if self.ardCom and self.ardCom.isOpen():
            self.ardCom.close()
            self.ui.txtSerial.append("Conexión cerrada.")
            self.ui.btnDisconnect.setEnabled(False)
            self.ui.btnSend.setEnabled(False)
            self.ui.txtMessage.setReadOnly(True)
            self.ui.cbCOM.setEnabled(True)
            self.ui.cbBaudrate.setEnabled(True)
            self.ui.btnUpdate.setEnabled(True)
            self.ui.btnConnect.setEnabled(True)
            if self.serial_reader:
                self.serial_reader.stop()
                self.serial_reader.wait()
                self.serial_reader = None
        else:
            self.ui.txtSerial.append("No hay conexión abierta.")

    def send(self):
        if self.ardCom and self.ardCom.isOpen():
            message = self.ui.txtMessage.toPlainText() + '\n'
            self.ardCom.write(message.encode("utf-8"))
            self.ui.txtSerial.append(f"< {message.strip()}")
        else:
            self.ui.txtSerial.append("No hay conexión abierta.")
        self.ui.txtMessage.clear()


    def update_textbox(self, message):
        self.ui.txtSerial.append("> " + message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySerialApp()
    window.show()
    sys.exit(app.exec())