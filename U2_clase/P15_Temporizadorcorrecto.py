from PyQt5 import uic, QtWidgets, QtCore

import sys
qtCreatorFile = "P15_TemporizadorCorrecto.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals

        self.lcdNumber.setNumberDigits(4)
        self.valor_inicial = 10
        self.lcdNumber.display(self.valor_inicial)

        self.btn_iniciar.clicked.connect(self.iniciar)

        self.hiloSegundoPlano= QtCore.Qtime()
        self.hiloSegundoPlano.timeout.connect(self.contar)

    def iniciar(self):
        self.valor_inicial=10
        self.hiloSegundoPlano.start(250)

    # Área de los Slots
    def contar(self):
         print(self.valor_inicial)
         self.lcdNumber.display(self.valor_inicial)
         self.valor_inicial-=1
         if self.valor_inicial== -1:
            self.hiloSegundoplano.stop



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
