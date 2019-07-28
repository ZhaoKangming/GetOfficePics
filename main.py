# -*- coding: utf-8 -*-

"""
author: ZhaoKangming
E-Mail: zhaokm0@gmail.com
"""


import sys
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GetOfficePics import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self,parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)


    # 菜单栏函数
    def openGithub(self):
        webbrowser.open("https://github.com/ZhaoKangming/GetOfficePics")

    def copyEmail(self):
        Email_dialog = QDialog()
        Email_dialog.resize(300, 80)
        Email_label = QLabel(Email_dialog)
        Email_label.setText("<font face='Microsoft YaHei' size='4'>zhaokm0@gmail.com</font>")
        Email_label.move(30,20)
        CopyEmail_btn = QPushButton('复制',Email_dialog)
        CopyEmail_btn.move(200,20)
        # self.CopyEmail_btn.clicked.connect()
        # CopyEmail_btn.setText("<b><font face='Microsoft YaHei' size='3' color = 'green'>已复制</font></b>")
        Email_dialog.setWindowTitle("复制邮箱地址")
        Email_dialog.setWindowModality(Qt.ApplicationModal)
        
        Email_dialog.exec()


    def helpbook(self):
        helpContent =   "<p>【<b>功能</b>】无损提取Office文件中的图片</p>" \
                        "<p></p>" \
                        "<p>【<b>支持格式</b>】xls、xlsx、doc、docx、ppt、pptx</p>"
        QMessageBox.information(self,'使用说明',helpContent, QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_()) 


