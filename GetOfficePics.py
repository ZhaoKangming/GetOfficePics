# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\A\OneDrive\Github\GetOfficePics\GetOfficePics.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../../../.designer/backup/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.getPic_btn = QtWidgets.QPushButton(self.centralwidget)
        self.getPic_btn.setGeometry(QtCore.QRect(240, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.getPic_btn.setFont(font)
        self.getPic_btn.setObjectName("getPic_btn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 270, 166, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resources/pic/emoji1.jpg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/pic/emoji2.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("resources/pic/emoji3.jpg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 40, 431, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.getFile_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.getFile_label.setFont(font)
        self.getFile_label.setObjectName("getFile_label")
        self.horizontalLayout_2.addWidget(self.getFile_label)
        self.filePath_line = QtWidgets.QLineEdit(self.layoutWidget1)
        self.filePath_line.setObjectName("filePath_line")
        self.horizontalLayout_2.addWidget(self.filePath_line)
        self.getFile_btn = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(8)
        self.getFile_btn.setFont(font)
        self.getFile_btn.setObjectName("getFile_btn")
        self.horizontalLayout_2.addWidget(self.getFile_btn)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(51, 80, 431, 26))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.outPutpic_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.outPutpic_label.setFont(font)
        self.outPutpic_label.setObjectName("outPutpic_label")
        self.horizontalLayout_3.addWidget(self.outPutpic_label)
        self.picPath_line = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.picPath_line.setFont(font)
        self.picPath_line.setObjectName("picPath_line")
        self.horizontalLayout_3.addWidget(self.picPath_line)
        self.chooseFolder_btn = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(8)
        self.chooseFolder_btn.setFont(font)
        self.chooseFolder_btn.setObjectName("chooseFolder_btn")
        self.horizontalLayout_3.addWidget(self.chooseFolder_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        self.Settings_menu = QtWidgets.QMenu(self.menubar)
        self.Settings_menu.setObjectName("Settings_menu")
        self.FeedBack_menu = QtWidgets.QMenu(self.menubar)
        self.FeedBack_menu.setObjectName("FeedBack_menu")
        self.Help_menu = QtWidgets.QMenu(self.menubar)
        self.Help_menu.setObjectName("Help_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Github_action = QtWidgets.QAction(MainWindow)
        self.Github_action.setObjectName("Github_action")
        self.Email_action = QtWidgets.QAction(MainWindow)
        self.Email_action.setObjectName("Email_action")
        self.CheckUpdate_action = QtWidgets.QAction(MainWindow)
        self.CheckUpdate_action.setObjectName("CheckUpdate_action")
        self.Language_action = QtWidgets.QAction(MainWindow)
        self.Language_action.setObjectName("Language_action")
        self.DefaultFolder_action = QtWidgets.QAction(MainWindow)
        self.DefaultFolder_action.setObjectName("DefaultFolder_action")
        self.aboutProject_action = QtWidgets.QAction(MainWindow)
        self.aboutProject_action.setObjectName("aboutProject_action")
        self.Help_action = QtWidgets.QAction(MainWindow)
        self.Help_action.setObjectName("Help_action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.Settings_menu.addAction(self.Language_action)
        self.Settings_menu.addAction(self.DefaultFolder_action)
        self.FeedBack_menu.addAction(self.Github_action)
        self.FeedBack_menu.addAction(self.Email_action)
        self.FeedBack_menu.addSeparator()
        self.FeedBack_menu.addAction(self.CheckUpdate_action)
        self.Help_menu.addAction(self.Help_action)
        self.Help_menu.addSeparator()
        self.Help_menu.addAction(self.action_3)
        self.menubar.addAction(self.Settings_menu.menuAction())
        self.menubar.addAction(self.Help_menu.menuAction())
        self.menubar.addAction(self.FeedBack_menu.menuAction())

        # 信号连接
        self.Github_action.triggered.connect(self.openGithub)
        self.Email_action.triggered.connect(self.copyEmail)
        self.Help_action.triggered.connect(self.helpbook)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Office 文件无损提取图片"))
        self.getPic_btn.setText(_translate("MainWindow", "提取图片"))
        self.getFile_label.setText(_translate("MainWindow", "目标文件地址："))
        self.getFile_btn.setText(_translate("MainWindow", "选择文件"))
        self.outPutpic_label.setText(_translate("MainWindow", "图片输出地址："))
        self.picPath_line.setText(_translate("MainWindow", " (默认为源文件目录)"))
        self.chooseFolder_btn.setText(_translate("MainWindow", "选择文件夹"))
        self.Settings_menu.setTitle(_translate("MainWindow", "设置"))
        self.FeedBack_menu.setTitle(_translate("MainWindow", "反馈"))
        self.Help_menu.setTitle(_translate("MainWindow", "帮助"))
        self.Github_action.setText(_translate("MainWindow", "Github issue"))
        self.Email_action.setText(_translate("MainWindow", "E-mail"))
        self.CheckUpdate_action.setText(_translate("MainWindow", "检查更新"))
        self.Language_action.setText(_translate("MainWindow", "语言"))
        self.DefaultFolder_action.setText(_translate("MainWindow", "默认存储位置"))
        self.aboutProject_action.setText(_translate("MainWindow", "关于项目"))
        self.Help_action.setText(_translate("MainWindow", "使用说明"))
        self.action_3.setText(_translate("MainWindow", "关于项目"))
