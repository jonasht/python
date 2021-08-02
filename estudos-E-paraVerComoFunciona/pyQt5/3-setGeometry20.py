import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    w = QWidget()

    bt = QPushButton(w)
    bt.setText('ola mundo')
    bt.move(50, 20)
    bt.clicked.connect(bt_clicado)

    w.setGeometry(100, 100, 300, 100)
    w.setWindowTitle('pyqt5')

    w.show()
    sys.exit(app.exec_())
qtdbotao = 1
def bt_clicado():
    global qtdbotao
    print(f'botao clicado {qtdbotao} vezes')
    qtdbotao += 1

if __name__ == '__main__':
    window()

