# Form implementation generated from reading ui file 'Panel.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        icon = QtGui.QIcon.fromTheme("applications-system")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbCOM = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbCOM.setGeometry(QtCore.QRect(120, 60, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Nunito Light")
        font.setPointSize(12)
        self.cbCOM.setFont(font)
        self.cbCOM.setCurrentText("")
        self.cbCOM.setObjectName("cbCOM")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Nunito Medium")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.btnConnect = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnConnect.setGeometry(QtCore.QRect(10, 100, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Nunito Medium")
        font.setPointSize(10)
        self.btnConnect.setFont(font)
        self.btnConnect.setAutoFillBackground(False)
        self.btnConnect.setFlat(False)
        self.btnConnect.setObjectName("btnConnect")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.txtMessage = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtMessage.setGeometry(QtCore.QRect(100, 151, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito Light")
        font.setPointSize(10)
        self.txtMessage.setFont(font)
        self.txtMessage.setObjectName("txtMessage")
        self.txtMessage.setReadOnly(True)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito Medium")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.txtSerial = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtSerial.setGeometry(QtCore.QRect(20, 200, 361, 151))
        self.txtSerial.setObjectName("txtSerial")
        self.txtSerial.setReadOnly(True)
        self.btnDisconnect = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnDisconnect.setGeometry(QtCore.QRect(100, 100, 91, 24))
        font = QtGui.QFont()
        font.setFamily("Nunito Medium")
        font.setPointSize(10)
        self.btnDisconnect.setFont(font)
        self.btnDisconnect.setObjectName("btnDisconnect")
        self.btnDisconnect.setEnabled(False)
        self.btnUpdate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(200, 100, 91, 24))
        font = QtGui.QFont()
        font.setFamily("Nunito Medium")
        font.setPointSize(10)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnSend = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(300, 100, 91, 24))
        font = QtGui.QFont()
        font.setFamily("Nunito Medium")
        font.setPointSize(10)
        self.btnSend.setFont(font)
        self.btnSend.setObjectName("btnSend")
        self.btnSend.setEnabled(False)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Nunito Medium")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.cbBaudrate = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbBaudrate.setGeometry(QtCore.QRect(300, 60, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Nunito Light")
        font.setPointSize(12)
        self.cbBaudrate.setFont(font)
        self.cbBaudrate.setObjectName("cbBaudrate")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        self.cbBaudrate.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SerialApp"))
        self.label.setText(_translate("MainWindow", "Puerto COM"))
        self.btnConnect.setText(_translate("MainWindow", "Conectar"))
        self.label_2.setText(_translate("MainWindow", "Comunicación Serial"))
        self.label_3.setText(_translate("MainWindow", "Mensaje"))
        self.btnDisconnect.setText(_translate("MainWindow", "Desconectar"))
        self.btnUpdate.setText(_translate("MainWindow", "Actualizar"))
        self.btnSend.setText(_translate("MainWindow", "Enviar"))
        self.label_4.setText(_translate("MainWindow", "Baudrate"))
        self.cbBaudrate.setItemText(0, _translate("MainWindow", "300"))
        self.cbBaudrate.setItemText(1, _translate("MainWindow", "600"))
        self.cbBaudrate.setItemText(2, _translate("MainWindow", "1200"))
        self.cbBaudrate.setItemText(3, _translate("MainWindow", "2400"))
        self.cbBaudrate.setItemText(4, _translate("MainWindow", "4800"))
        self.cbBaudrate.setItemText(5, _translate("MainWindow", "9600"))
        self.cbBaudrate.setItemText(6, _translate("MainWindow", "14400"))
        self.cbBaudrate.setItemText(7, _translate("MainWindow", "19200"))
        self.cbBaudrate.setItemText(8, _translate("MainWindow", "38400"))
        self.cbBaudrate.setItemText(9, _translate("MainWindow", "57600"))
        self.cbBaudrate.setItemText(10, _translate("MainWindow", "115200"))
        self.cbBaudrate.setItemText(11, _translate("MainWindow", "230400"))
        self.cbBaudrate.setItemText(12, _translate("MainWindow", "460800"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
