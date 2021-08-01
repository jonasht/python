from PyQt5.QtWidgets import *
import sys


class Janela(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.btgr = QButtonGroup()
        self.btgr.setExclusive(False)
        self.btgr.buttonClicked[int].connect(self.botao_clicado)

        bt = QPushButton('botao 1')
        self.btgr.addButton(bt, 1)
        layout.addWidget(bt)

        bt = QPushButton('botao 2')
        self.btgr.addButton(bt, 2)
        layout.addWidget(bt)

    def botao_clicado(self, id):
        for bt in self.btgr.buttons():
            if bt is self.btgr.button(id):
                print(f'o botao {bt.text()} foi clicado')

app = QApplication(sys.argv)

tela = Janela()
tela.show()

sys.exit(app.exec())
