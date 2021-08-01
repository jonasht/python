from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        lb = QLabel('focus combox e aperte shift+f1')
        layout.addWidget(lb)

        self.combobox = QComboBox()
        self.combobox.setWhatsThis('este é uma descricao de "whatsThis"' )
        layout.addWidget(self.combobox)

app = QApplication(sys.argv)

tela = Window()
tela.show()

sys.exit(app.exec())
