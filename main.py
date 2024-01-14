import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QMessageBox, QApplication
from login import Login
from signup import Signup
from splash import Splash
from forgotPassword import ForgotPassword
from pymongo import MongoClient


class anaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["tahatones"]
        self.users_collection = self.db["users"]

        self.vlayout = QVBoxLayout(self)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(977, 692)

        self.loginWidget = QWidget()
        self.signupWidget = QWidget()
        self.splashWidget = QWidget()
        self.forgotPasswordWidget = QWidget()

        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.addWidget(self.signupWidget)
        self.stackedWidget.addWidget(self.splashWidget)
        self.stackedWidget.addWidget(self.forgotPasswordWidget)

        self.vlayout.addWidget(self.stackedWidget)

        self.splashPage()
        self.signupPage()
        self.loginPage()
        self.forgotPage()
        self.stackedWidget.setCurrentIndex(2)

    def splashPage(self):
        self.splash_Form = Splash()
        self.splash_Form.setupUi(self.splashWidget)
        self.gosignupbutton = self.splash_Form.signupBtn
        self.gologinbutton = self.splash_Form.loginBtn
        self.gologinbutton.clicked.connect(self.showLoginPage)
        self.gosignupbutton.clicked.connect(self.showsignupPage)

    def signupPage(self):
        self.signup_Form = Signup()
        self.signup_Form.setupUi(self.signupWidget)
        self.signupbutton = self.signup_Form.signupBtn
        self.gologinbutton2 = self.signup_Form.loginBtn
        self.gologinbutton2.clicked.connect(self.showLoginPage)
        self.signupbutton.clicked.connect(self.signupfunction)

    def loginPage(self):
        self.login_Form = Login()
        self.login_Form.setupUi(self.loginWidget)
        self.gosignupbutton2 = self.login_Form.signupBtn
        self.loginbutton = self.login_Form.loginBtn
        self.goforgotbutton = self.login_Form.pushButton
        self.gosignupbutton2.clicked.connect(self.showsignupPage)
        self.goforgotbutton.clicked.connect(self.showForgotPage)
        self.loginbutton.clicked.connect(self.loginfunction)

    def forgotPage(self):
        self.forgot_Form = ForgotPassword()
        self.forgot_Form.setupUi(self.forgotPasswordWidget)
        self.forgotbutton = self.forgot_Form.forgotpassBtn
        self.gologinbutton3 = self.forgot_Form.loginBtn
        self.gologinbutton3.clicked.connect(self.showLoginPage)
        self.forgotbutton.clicked.connect(self.forgotfunction)

    def loginfunction(self):
        password = self.login_Form.lineEdit_2.text().strip()
        email = self.login_Form.lineEdit.text().strip()
        if not (email and password):
            QMessageBox.warning(self, "Warning", "Please enter username and password.")
            return

        # Check if the user exists in the database
        user = self.users_collection.find_one({"email": email})

        if user and 'password' in user:
            QMessageBox.information(self, "Success", "Login successful!")
            self.stackedWidget.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

    def signupfunction(self):
        password = self.signup_Form.lineEdit_2.text().strip()
        email = self.signup_Form.lineEdit.text().strip()

        user_data = {
            "password": password,
            "email": email,
        }
        if self.users_collection.find_one({"email": email}):
            QMessageBox.warning(self, "Warning", "Email already taken. Please choose another.")
            return
        else:
            self.users_collection.insert_one(user_data)
            QMessageBox.information(self, "Success", "Registration successful!")
            self.stackedWidget.setCurrentIndex(0)

    def forgotfunction(self):
        email = self.forgot_Form.lineEdit.text().strip()

        if not email:
            QMessageBox.warning(self, "Warning", "Please enter a username or email.")
            return

        user = self.users_collection.find_one({"$or": {"email": email}})

        if user:
            QMessageBox.information(self, "Success", "Password reset link sent to your email.")
            self.stackedWidget.setCurrentIndex(0)

        else:
            QMessageBox.warning(self, "Error", "Username or email not found in the database.")

    def showLoginPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def showForgotPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def showsignupPage(self):
        self.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = anaPencere()
    window.show()
    sys.exit(app.exec())