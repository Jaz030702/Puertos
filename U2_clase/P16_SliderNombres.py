from PyQt5 import uic, QtWidgets, QtCore

import sys
qtCreatorFile = "P16_SliderNombres.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals

        self.lista_nombres = [
            "pedro" "Gael" "angel" "carlos" "Diego"
        ]
        self.index_nombre = 0
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])
        self.txt_nombre.setEnabled(False)
        self.btn_iniciar.clicked.connect(self.iniciar)

        self.hiloSegundoPlano= QtCore.QTimer()
        self.hiloSegundoPlano.timeout.connect(self.contar)

    def iniciar(self):
        self.index_nombre=0
        self.index_nombre.start(550)

    # Área de los Slots
    def contar(self):
        self.index_nombre+=1

        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
