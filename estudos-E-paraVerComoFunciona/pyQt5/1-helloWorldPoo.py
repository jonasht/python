import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class window(QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.resize(200, 50)
        self.setWindowTitle('hello')

        self.lb = QLabel(self, text='hello world')
        font =  QFont()
        font.setFamily('Arial')
        font.setPointSize(18)
        self.lb.setFont(font)
        self.lb.move(50, 20)
        

        
def main():
    
    app = QApplication(sys.argv)
    tela = window()
    tela.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    