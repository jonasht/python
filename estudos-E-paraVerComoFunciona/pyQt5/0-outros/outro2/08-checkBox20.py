from PyQt5.QtWidgets import *

import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox1 = QCheckBox('algo 1')
        self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 0,0)

        self.checkbox2 = QCheckBox('algo 2')
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 1 ,0)

        self.checkbox3 = QCheckBox('algo 3')
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 2,0)

    def checkbox_toggled(self):
        selecionados = []

        if self.checkbox1.isChecked():
            selecionados.append('algo 1')
        if self.checkbox2.isChecked():
            selecionados.append('algo 2')

        if self.checkbox3.isChecked():
            selecionados.append('algo 3')
        
        print(f'selecionados: {" ".join(selecionados)}')

app = QApplication(sys.argv)

tela = Window()
tela.show()

sys.exit(app.exec_())

        