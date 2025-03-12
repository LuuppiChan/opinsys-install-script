import os
import sys

from PySide6 import QtWidgets, QtCore, QtGui

if True:
    os.system("pyside6-uic main.ui -o ui.py")  # for rapid prototyping
    from ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_asenna.clicked.connect(self.asennus)
        self.ui.pushButton_poista.clicked.connect(self.poisto)

    def asennus(self):
        # setup
        os.makedirs("/tmp/opinsys-install", exist_ok=True)

        match self.ui.comboBox_ohjelmat_asennus.currentText():
            case "Steam":
                os.system("wget https://cdn.akamai.steamstatic.com/client/installer/steam.deb ")

                pass
            case "Minecraft Launcher":
                pass
            case "Discord":
                pass
            case "Vesktop":
                pass
            case "Brave":
                pass
            case "Paketin hallinta":
                pass

    def poisto(self):
        match self.ui.comboBox_ohjelmat_asennus.currentText():
            case "Steam":
                pass
            case "Minecraft Launcher":
                pass
            case "Discord":
                pass
            case "Vesktop":
                pass
            case "Brave":
                pass
            case "Paketin hallinta":
                pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    style_name = app.style().metaObject().className()
    if style_name == "QFusionStyle":
        palette = QtGui.QPalette()  # it works so it's fine
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Link, QtGui.QColor(218, 130, 218))
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(218, 130, 218))
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
