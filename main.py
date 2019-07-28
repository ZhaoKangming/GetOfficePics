# -*- coding: utf-8 -*-

"""
author: ZhaoKangming
E-Mail: zhaokm0@gmail.com
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from GetOfficePics import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self,parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def on_getPic_btn_clicked(self):
        self.label_4.setText("哇，成功了！")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_()) 


