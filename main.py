from PyQt5 import QtGui
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from principal import Ui_Principal


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)

        self.ui.btnPrincipal.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.principal)
        )
        self.ui.btnUsuarios.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.usuarios)
        )
        self.ui.btnConfiguracion.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.configuracion)
        )

        self.ui.btnMenu.clicked.connect(self.expandir)

    def expandir(self):
        ancho = self.ui.menuIzquierdo.width()
        if ancho == 50:
            nuevoAncho = 180
            self.ui.btnMenu.setIcon(QtGui.QIcon(
                ":/Iconos/Iconos/Contraer.png"))
        elif ancho == 180:
            nuevoAncho = 50
            self.ui.btnMenu.setIcon(QtGui.QIcon(
                ":/Iconos/Iconos/Menu.png"))

        try:
            self.animacion = QPropertyAnimation(
                self.ui.menuIzquierdo, b"minimumWidth")
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(nuevoAncho)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()

        except:
            self.ui.btnMenu.setIcon(QtGui.QIcon(
                ":/Iconos/Iconos/Menu.png"))
            self.animacion.setStartValue(50)
            self.animacion.setEndValue(50)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())
