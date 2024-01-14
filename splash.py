from PyQt6 import QtCore, QtGui, QtWidgets


class Splash(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(977, 692)
        Form.setStyleSheet("\n"
"\n"
"#bottomMenu QPushButton{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setStyleSheet("#widget{border-image: url(:/arkaplan/3.1.jpg);}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topMenu = QtWidgets.QWidget(parent=self.widget)
        self.topMenu.setObjectName("topMenu")
        self.midMenu = QtWidgets.QWidget(parent=self.topMenu)
        self.midMenu.setGeometry(QtCore.QRect(9, 125, 925, 201))
        self.midMenu.setObjectName("midMenu")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.midMenu)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 30, 741, 171))
        self.textBrowser_3.setStyleSheet("background: transparent;\n"
"border: none;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.upperMenu = QtWidgets.QWidget(parent=self.topMenu)
        self.upperMenu.setGeometry(QtCore.QRect(9, 9, 925, 101))
        self.upperMenu.setObjectName("upperMenu")
        self.upperLeftMenu = QtWidgets.QWidget(parent=self.upperMenu)
        self.upperLeftMenu.setGeometry(QtCore.QRect(10, 10, 451, 80))
        self.upperLeftMenu.setObjectName("upperLeftMenu")
        self.label_4 = QtWidgets.QLabel(parent=self.upperLeftMenu)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 49, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.upperLeftMenu)
        self.label_5.setGeometry(QtCore.QRect(75, 10, 51, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: red;\n"
"")
        self.label_5.setObjectName("label_5")
        self.upperRightMenu = QtWidgets.QWidget(parent=self.upperMenu)
        self.upperRightMenu.setGeometry(QtCore.QRect(470, 10, 451, 80))
        self.upperRightMenu.setObjectName("upperRightMenu")
        self.verticalLayout_2.addWidget(self.topMenu)
        self.bottomMenu = QtWidgets.QWidget(parent=self.widget)
        self.bottomMenu.setObjectName("bottomMenu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottomMenu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signUpMenu = QtWidgets.QWidget(parent=self.bottomMenu)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.signUpMenu.setFont(font)
        self.signUpMenu.setObjectName("signUpMenu")
        self.signupBtn = QtWidgets.QPushButton(parent=self.signUpMenu)
        self.signupBtn.setGeometry(QtCore.QRect(40, 250, 140, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signupBtn.sizePolicy().hasHeightForWidth())
        self.signupBtn.setSizePolicy(sizePolicy)
        self.signupBtn.setStyleSheet("")
        self.signupBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/yeniÖnek/icons/icons8-dumbbell-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.signupBtn.setIcon(icon)
        self.signupBtn.setIconSize(QtCore.QSize(40, 40))
        self.signupBtn.setObjectName("signupBtn")
        self.label = QtWidgets.QLabel(parent=self.signUpMenu)
        self.label.setGeometry(QtCore.QRect(40, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.signUpMenu)
        self.textBrowser.setGeometry(QtCore.QRect(40, 140, 361, 101))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
"border: none;")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.signUpMenu)
        self.loginMenu = QtWidgets.QWidget(parent=self.bottomMenu)
        self.loginMenu.setEnabled(True)
        self.loginMenu.setObjectName("loginMenu")
        self.loginBtn = QtWidgets.QPushButton(parent=self.loginMenu)
        self.loginBtn.setGeometry(QtCore.QRect(40, 250, 140, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy)
        self.loginBtn.setStyleSheet("")
        self.loginBtn.setText("")
        self.loginBtn.setIcon(icon)
        self.loginBtn.setIconSize(QtCore.QSize(40, 40))
        self.loginBtn.setObjectName("loginBtn")
        self.label_2 = QtWidgets.QLabel(parent=self.loginMenu)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"")
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.loginMenu)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 140, 361, 101))
        self.textBrowser_2.setStyleSheet("background-color: transparent;\n"
"border: none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout.addWidget(self.loginMenu)
        self.verticalLayout_2.addWidget(self.bottomMenu)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Workout, the most delicious and crucial meal on your table.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">As it decreases, you\'ll wither with the fear of going hungry.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Therefore, you\'ll age.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Because, from the beginning to the end, you too will eventually conclude.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Even if you\'re the trillion, you\'ll be spent.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Cease the sedantary life, embrace exercise.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">You\'ll negotiate with yourself in the mirrors.</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "Ta Ha"))
        self.label_5.setText(_translate("Form", "Tones"))
        self.label.setText(_translate("Form", "SINGUP"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">Create your account now to embark on your fitness journey and enjoy exclusive features.</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "LOGIN"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">Access your account to unlock personalized fitness experiences and track your progress.</span></p></body></html>"))
