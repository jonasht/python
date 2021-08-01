from sys import exit, argv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(argv)

    widget = QWidget()

    lb = QLabel(widget)
    lb.setText('ola mundo')
    lb.move(50, 50)
    
    widget.setWindowTitle('hello')
    widget.show()
    exit(app.exec_())
    
if __name__ == '__main__':
    window()