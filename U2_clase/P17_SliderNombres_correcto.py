from PyQt5 import uic, QtWidgets, QtCore
import sys
import random as rnd

qtCreatorFile = "P16_SliderNombres.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Lista de nombres
        self.lista_nombres = ["puertos", "sistemas", "base de datos ", "Virtual", "valores"]
        self.index_nombre = 0
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])
        self.txt_nombre.setEnabled(False)

        # Conexión de señales
        self.btn_iniciar.clicked.connect(self.control)

        # Timer
        self.hiloSegundoPlano = QtCore.QTimer()
        self.hiloSegundoPlano.timeout.connect(self.actualizar_nombre)
    def control(self):
        texto_boton = self.btn_iniciar.text()
        if texto_boton == "INICIAR":
            self.index_nombre = 0
            self.hiloSegundoPlano.start(550)
            self.btn_iniciar.setText("DETENER")
        else:
            self.hiloSegundoPlano.stop()
            self.btn_iniciar.setText("INICIAR")
    def actualizar_nombre(self):
        self.index_nombre += 1
        if self.index_nombre >= len(self.lista_nombres):
            self.index_nombre = 0
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
