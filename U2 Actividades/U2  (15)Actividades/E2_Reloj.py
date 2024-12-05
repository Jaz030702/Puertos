import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E2_Reloj.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.horas_actual = 0
        self.minutos_actual = 0

        self.lcdHoras.setNumDigits(2)
        self.lcdMin.setNumDigits(2)
        self.lcdHoras.display(self.horas_actual)
        self.lcdMin.display(self.minutos_actual)

        self.spbHoras.setMinimum(0)
        self.spbHoras.setMaximum(23)
        self.spbHoras.setSingleStep(1)
        self.spbHoras.setValue(0)

        self.spbMin.setMinimum(0)
        self.spbMin.setMaximum(59)
        self.spbMin.setSingleStep(1)
        self.spbMin.setValue(0)

        self.spbHoras.valueChanged.connect(self.cambiarPeriodo)

        self.hora_alarma = -1
        self.min_alarma = -1
        self.btnAlarma.clicked.connect(self.configurarAlarma)

        self.temporizador = QtCore.QTimer()
        self.temporizador.timeout.connect(self.incrementarMinutos)
        self.temporizador.start(10)

        # Cambiar el color de fondo a amarillo
        self.setStyleSheet("background-color: yellow;")

    # Área de los Slots
    def configurarAlarma(self):
        if self.btnAlarma.text() == "AGREGAR":
            self.hora_alarma = int(self.spbHoras.value())
            self.min_alarma = int(self.spbMin.value())
            self.spbHoras.setEnabled(False)
            self.spbMin.setEnabled(False)
            self.btnAlarma.setText("ELIMINAR")
        else:
            self.hora_alarma = -1
            self.min_alarma = -1
            self.spbHoras.setEnabled(True)
            self.spbMin.setEnabled(True)
            self.btnAlarma.setText("AGREGAR")

    def cambiarPeriodo(self):
        if self.spbHoras.value() < 13:
            self.lblAMPM2.setText("A.M.")
        else:
            self.lblAMPM2.setText("P.M.")

    def incrementarMinutos(self):
        self.lcdMin.display(self.minutos_actual)
        self.lcdHoras.display(self.horas_actual)
        self.minutos_actual += 1
        if self.minutos_actual == 60:
            self.minutos_actual = 0
            self.horas_actual += 1
        if self.horas_actual == 24:
            self.horas_actual = 0
        if self.horas_actual < 13:
            self.lblAMPM1.setText("A.M.")
        else:
            self.lblAMPM1.setText("P.M.")
        if self.horas_actual == self.hora_alarma and self.minutos_actual == self.min_alarma:
            self.mostrarMensaje("Alarma")

    def mostrarMensaje(self, texto):
        mensaje = QtWidgets.QMessageBox()
        mensaje.setText(texto)
        mensaje.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
