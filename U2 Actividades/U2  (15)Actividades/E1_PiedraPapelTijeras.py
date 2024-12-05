import random
import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "E1_PiedraPapelTijeras.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.puntuacion = 0
        self.opciones = ["Piedra", "Papel", "Tijera"]
        self.diccImgs = {
            "Piedra": ":/PPT/piedra.jpg",
            "Papel": ":/PPT/papel.jpg",
            "Tijera": ":/PPT/tijeras.jpg"
        }
        # Área de los Signals
        self.btnPiedra.clicked.connect(self.seleccion)
        self.btnPapel.clicked.connect(self.seleccion)
        self.btnTijera.clicked.connect(self.seleccion)

    # Área de los Slots
    def seleccion(self):
        obj = self.sender()
        o = obj.text()
        self.lbImgJugador.setPixmap(QtGui.QPixmap(self.diccImgs[o]))
        c = self.seleccionCPU()
        self.comparacion(o, c)

    def seleccionCPU(self):
        s = self.opciones[random.randrange(0, 3)]
        self.txtCPU.setText(s)
        self.lbImgCPU.setPixmap(QtGui.QPixmap(self.diccImgs[s]))
        return s

    def comparacion(self, j, c):
        m = ""
        color = ""
        if j == c:
            m = "Empate"
            color = "orange"

        elif j == "Piedra" and c == "Tijera":
            m = "El Jugador gano!"
            self.puntuacion += 1
            color = "green"
        elif j == "Piedra" and c == "Papel":
            m = "El Jugador perdio!"
            color = "red"

        elif j == "Papel" and c == "Piedra":
            m = "El Jugador gano!"
            self.puntuacion += 1
            color = "green"
        elif j == "Papel" and c == "Tijera":
            m = "El Jugador perdio!"
            color = "red"

        elif j == "Tijera" and c == "Papel":
            m = "El Jugador gano!"
            self.puntuacion += 1
            color = "green"
        elif j == "Tijera" and c == "Piedra":
            m = "El Jugador perdio!"
            color = "red"

        self.txtPuntos.setText(str(self.puntuacion))
        self.txtPuntos.setStyleSheet(f"color: {color};")  # Cambiar el color del texto
        self.mensaje(m, color)

    def mensaje(self, texto, color):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.setStyleSheet(f"color: {color};")  # Cambiar el color del mensaje
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


