from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QWidgetItem

app = QApplication([])

janela = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('TOP/cima'))
layout.addWidget(QPushButton('bottom/baixo'))
janela.setLayout(layout)
janela.show()

app.exec()