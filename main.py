from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys

FORM,_ = loadUiType('untitled.ui')
class main(QMainWindow, FORM):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.ui_changes()
        self.controllers()

    def ui_changes(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def controllers(self):
        self.pushButton_2.clicked.connect(self.order)
        self.pushButton.clicked.connect(self.reset)
        self.pushButton_3.clicked.connect(self.close_btn)

    def order(self):
        total = 0
        I3 = 0
        if self.checkBox.isChecked():
            total += 50 * self.spinBox.value()
        if self.checkBox_2.isChecked() == True:
            total += 400 * self.spinBox_2.value()
        if self.checkBox_3.isChecked() == True:
            total += 300 * self.spinBox_3.value()
        if self.checkBox_4.isChecked() == True:
            total += 200 * self.spinBox_4.value()
        if self.checkBox_5.isChecked() == True:
            total += 100 * self.spinBox_5.value()
        if self.checkBox_6.isChecked() == True:
            total += 50 * self.spinBox_6.value()
        I3 = total + (total* int(self.comboBox.currentText())/100)
        self.label_6.setText(str(total)+' Rs')
        self.label_7.setText(str(I3))

    def reset(self):
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)

        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_4.setValue(0)
        self.spinBox_5.setValue(0)
        self.spinBox_6.setValue(0)

        self.label_6.setText('')
        self.label_7.setText('')
        self.comboBox.setCurrentText('5')

    def close_btn(self):
        self.close()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    app.exec()