import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    botao1 = QPushButton('botao 1')
    botao2 = QPushButton('botao 2')
    botao1.clicked.connect(botao1_clicado)
    botao2.clicked.connect(botao2_clicado)
    
    hbox = QHBoxLayout()
    
    hbox.addWidget(botao1)
    hbox.addStretch()
    
    hbox.addWidget(botao2)
    win.setLayout(hbox)
    win.setWindowTitle('pyqt')
    win.show()


    sys.exit(app.exec_())

def botao1_clicado():
    print('botao 1 clicado')
def botao2_clicado():
    print('batao 2 clicado')

if __name__ == '__main__':
    window()