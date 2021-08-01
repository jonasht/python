from sys import exit, argv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QGridLayout()
        self.setLayout(layout)

        slider = QSlider(Qt.Horizontal)
        slider.setValue(20) # eh qtd que preenche o slider 
        layout.addWidget(slider, 0, 0)

        slider = QSlider(Qt.Vertical)
        slider.setValue(4) # eh qtd que preenche o slider 
        layout.addWidget(slider, 0, 1)
        
        
app = QApplication(argv) 
    

tela = Window()
tela.show()

exit(app.exec_())
        