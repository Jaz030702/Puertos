import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P26_ComboBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.dicc_alumnos = {
            "2206":["Luis", "IN", 20],
            "ANG":["Angel", "ISC", 22],
            "DIEG":["Diego", "IC", 21],
            "DAAY": ["Daylaan", "ISC", 24]
        }
        self.cb_alumnos.addItem("Luis", "2206")
        self.cb_alumnos.addItem("Daylaan", "DAAY")
        self.cb_alumnos.addItem("Diego", "DIEG")
        self.cb_alumnos.addItem("Angel", "ANG ")

        #tres formas de acceder a los elementos de un combobox...
        #texto - es lo que ve el usuario
        #data - clave
        #indice
        self.cb_alumnos.currentIndexChanged.connect(self.cambiaIndice)

    # Área de los Slots
    def cambiaIndice(self):
        texto = self.cb_alumnos.currentText()
        data = self.cb_alumnos.currentData()
        indice = self.cb_alumnos.currentIndex()
        print(texto + " - " + data + " - " + str(indice))
        self.cargaDatos(data) #data = clave

    def cargaDatos(self, clave):
        alumno = self.dicc_alumnos[clave]
        self.txt_nombre.setText(alumno[0])
        self.txt_carrera.setText(alumno[1])
        self.txt_edad.setText(str(alumno[2]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())