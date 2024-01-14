from PyQt6 import QtCore, QtGui, QtWidgets


class ForgotPassword(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 692)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    border-image: url(:/arkaplan/1.1.1.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 60, 120, 80))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(290, 250, 120, 80))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(420, 530, 120, 80))
        self.widget_3.setObjectName("widget_3")
        self.midMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.midMenu.setGeometry(QtCore.QRect(0, 257, 959, 131))
        self.midMenu.setStyleSheet("background: transparent;")
        self.midMenu.setObjectName("midMenu")
        self.label_2 = QtWidgets.QLabel(parent=self.midMenu)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : white;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.midMenu)
        self.lineEdit.setGeometry(QtCore.QRect(330, 50, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 10);\n"
"border: none;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.bottomMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.bottomMenu.setGeometry(QtCore.QRect(0, 404, 959, 271))
        self.bottomMenu.setObjectName("bottomMenu")
        self.forgotpassBtn = QtWidgets.QPushButton(parent=self.bottomMenu)
        self.forgotpassBtn.setGeometry(QtCore.QRect(410, 0, 140, 35))
        self.forgotpassBtn.setStyleSheet("    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0);")
        self.forgotpassBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/yeniÖnek/icons/icons8-dumbbell-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.forgotpassBtn.setIcon(icon)
        self.forgotpassBtn.setIconSize(QtCore.QSize(40, 40))
        self.forgotpassBtn.setObjectName("forgotpassBtn")
        self.loginBtn = QtWidgets.QPushButton(parent=self.bottomMenu)
        self.loginBtn.setGeometry(QtCore.QRect(440, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("color : red;\n"
"background : transparent;")
        self.loginBtn.setObjectName("loginBtn")
        self.topMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.topMenu.setGeometry(QtCore.QRect(0, 0, 959, 241))
        self.topMenu.setObjectName("topMenu")
        self.label = QtWidgets.QLabel(parent=self.topMenu)
        self.label.setGeometry(QtCore.QRect(390, 180, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color : white;")
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "e-mail adress"))
        self.loginBtn.setText(_translate("MainWindow", "Log in"))
        self.label.setText(_translate("MainWindow", "FORGOT PASSWORD"))
