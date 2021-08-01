from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton('brasil')
        radiobutton.setChecked(True) # eh p ficar radio ficar marcado

        radiobutton.country = 'Brazil'
        radiobutton.toggled.connect(self.on_radio_button_toggeled)
        layout.addWidget(radiobutton, 0,0)

        radiobutton = QRadioButton('argentina')
        radiobutton.country = 'argentina'
        radiobutton.toggled.connect(self.on_radio_button_toggeled)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton('ecuador')
        radiobutton.country = 'ecuador'
        radiobutton.toggled.connect(self.on_radio_button_toggeled)
        layout.addWidget(radiobutton, 0,2)

    def on_radio_button_toggeled(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
                print(f'pais selecionado: {radiobutton.country}')

app = QApplication(sys.argv)
tela = Window()
tela.show()

sys.exit(app.exec_())