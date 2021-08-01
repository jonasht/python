from sys import exit, argv
from PyQt5.QtWidgets import *


def window():
    app = QApplication(argv)

    w = QWidget()
    b = QLabel(w)
    b.setText('hello world')
    w.setGeometry(100,100,200,100)
    b.move(50, 60)
    w.setWindowTitle('PyQt')
    
    lb = QLabel(w, text='ola mundo')
    lb.move(50, 40)
    lb2 = QLabel(w, text='oi')
    lb2.move(60, 80)
    w.show()
    exit(app.exec_())

if __name__ == '__main__':
    window()