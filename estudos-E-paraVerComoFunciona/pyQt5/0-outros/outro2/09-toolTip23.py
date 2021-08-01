from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        bt = QPushButton('clique em mim')
        bt.clicked.connect(self.botao_apertado)
        bt.setToolTip('por favor nao clique')
        layout.addWidget(bt, 0,0)
        
        bt2 = QPushButton('toolTip simples')
        bt2.setToolTip('este tooltip mostra texto')
        layout.addWidget(bt2, 1, 0)


    def botao_apertado(self):
        print('botao foi clicado')

app = QApplication(sys.argv)

tela = Window()
tela.show()

sys.exit(app.exec_())