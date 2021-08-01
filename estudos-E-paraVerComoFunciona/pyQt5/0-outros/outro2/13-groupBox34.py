import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class GroupBox(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('groupbox')

        
        layout = QGridLayout()
        self.setLayout(layout)

        groupbox = QGroupBox('Group exemplo')
        groupbox.setCheckable(True) # eh p o radio ficar marcado
        layout.addWidget(groupbox)

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        radiobt = QRadioButton('radioButton-1')
        radiobt.setChecked(True) # eh para ficar Radio ficar marcado
        vbox.addWidget(radiobt)
        
        radiobt = QRadioButton('radiobutton-2')
        vbox.addWidget(radiobt)

app = QApplication(sys.argv)

tela = GroupBox()
tela.show()

sys.exit(app.exec_())
        