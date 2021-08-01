from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Janela(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel('a estoria de dale')
        layout.addWidget(label, 0, 0)

        label = QLabel('poucas pessoas puderam enteder a motivacao. nao foi algo ...')
        label.setWordWrap(True)

        layout.addWidget(label, 0,1)


app = QApplication(sys.argv)

tela = Janela()
tela.show()

sys.exit(app.exec_())
