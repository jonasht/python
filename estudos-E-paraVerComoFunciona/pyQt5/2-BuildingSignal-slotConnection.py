import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




def window():
    app = QApplication(sys.argv)
    win = QDialog()

    # definindo botao 1
    bt1 = QPushButton(win)
    bt1.setText('botao 1')
    bt1.move(50, 20)
    bt1.clicked.connect(bt1_clicado)

    # definindo botao 2
    bt2 = QPushButton(win)
    bt2.setText('botao 2')
    bt2.move(50, 50)
    bt2.clicked.connect(bt2_clicado)

    win.setGeometry(100,100,200,100)
    win.show()
    sys.exit(app.exec_())

def bt1_clicado():
    print('botao 1 foi clicado')
def bt2_clicado():
    print('botao 2 foi clicado')
    

if __name__ == '__main__':
    window()