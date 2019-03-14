from PyQt5 import QtWidgets,QtCore,QtGui
import sys
class yeni(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000,450)
        self.move(50,50)
        
        self.buton=QtWidgets.QPushButton("Buton",self)
        self.buton.move(10,100)
        
        self.label1=QtWidgets.QLabel("Ben Labelim",self)
        self.label1.move(15,125)

        self.textbox1=QtWidgets.QLineEdit(self)
        self.textbox1.move(10,75)
        
        
        self.buton.clicked.connect(self.tikla)
        
        
    def tikla(self, text):
        
        self.label1.setText(self.textbox1.text())


uygulama=QtWidgets.QApplication(sys.argv)
pencere=yeni()
pencere.show()
uygulama.exec_()
