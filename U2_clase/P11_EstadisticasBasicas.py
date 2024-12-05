import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P11_EstadisticaBasica.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_promedio.clicked.connect(self.operacion)
        self.btn_mediana.clicked.connect(self.operacion)
        self.btn_desviacion.clicked.connect(self.operacion)
        self.btn_varianza.clicked.connect(self.operacion)
        self.btn_valor_mayor.clicked.connect(self.operacion)
        self.btn_valor_menor.clicked.connect(self.operacion)

    # Área de los Slots
    def operacion(self):
        objeto=self.sender()
        nombre_objeto= objeto.objectName()
        print(nombre_objeto)
        numA = int(self.txt_A.text())
        numB = int(self.txt_B.text())
        if nombre_objeto== "btn_promedio": resultado =numA+numB
        elif nombre_objeto== "btn_resta": resultado =numA-numB
        elif nombre_objeto== "btn_multiplicar": resultado =numA* numB
        elif nombre_objeto== "btn_dividir": resultado =numA/ numB
        self.txt_resultado.setText(str(resultado))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
