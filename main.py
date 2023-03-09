from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle("Address Book")
        self.initUI()

    def initUI(self):
        # FIRST NAME
        self.fNameLabel = QtWidgets.QLabel(self)
        self.fNameLabel.setText("First Name:")
        self.fNameLabel.move(50, 50)
        
        self.fNameTextbox = QtWidgets.QLineEdit(self)
        self.fNameTextbox.move(50, 75)
        self.fNameTextbox.resize(500, 30)


        # LAST NAME
        self.lNameLabel = QtWidgets.QLabel(self)
        self.lNameLabel.setText("Last Name:")
        self.lNameLabel.move(50, 100)
        
        self.lNameTextbox = QtWidgets.QLineEdit(self) # creates a textbox
        self.lNameTextbox.move(50, 125)
        self.lNameTextbox.resize(500, 30)

        
        # ADDRESS
        self.addressLabel = QtWidgets.QLabel(self)
        self.addressLabel.setText("Address:")
        self.addressLabel.move(50, 150)
        
        self.addressTextbox = QtWidgets.QLineEdit(self) # creates a textbox
        self.addressTextbox.move(50, 175)
        self.addressTextbox.resize(500, 30)


        # CITY
        self.cityLabel = QtWidgets.QLabel(self)
        self.cityLabel.setText("City:")
        self.cityLabel.move(50, 200)
        
        self.cityTextbox = QtWidgets.QLineEdit(self) # creates a textbox
        self.cityTextbox.move(50, 225)
        self.cityTextbox.resize(500, 30)


        # POSTCODE
        self.postcodeLabel = QtWidgets.QLabel(self)
        self.postcodeLabel.setText("Postcode:")
        self.postcodeLabel.move(50, 250)
        
        self.postcodeTextbox = QtWidgets.QLineEdit(self) # creates a textbox
        self.postcodeTextbox.move(50, 275)
        self.postcodeTextbox.resize(500, 30)


        # PHONE NUMBER
        self.phoneNumberLabel = QtWidgets.QLabel(self)
        self.phoneNumberLabel.setText("Phone Number:")
        self.phoneNumberLabel.move(50, 300)
        
        self.phoneNumberTextbox = QtWidgets.QLineEdit(self) # creates a textbox
        self.phoneNumberTextbox.move(50, 325)
        self.phoneNumberTextbox.resize(500, 30)


        # EMAIL
        self.emailLabel = QtWidgets.QLabel(self)
        self.emailLabel.setText("Email Address:")
        self.emailLabel.move(50, 350)
        
        self.emailTextbox = QtWidgets.QLineEdit(self) # creates a textbox
        self.emailTextbox.move(50, 375)
        self.emailTextbox.resize(500, 30)

        
        
        # SUBMIT BUTTON
        self.submitButton = QtWidgets.QPushButton(self)
        self.submitButton.setText("Submit")
        self.submitButton.move(250, 500)
        self.submitButton.clicked.connect(self.submitForm)

        self.show()
    
    def submitForm(self):
        print("You have submitted this form with the following details:")
        print(self.fNameTextbox.text())
        print(self.lNameTextbox.text())
        print(self.addressTextbox.text())
        print(self.cityTextbox.text())
        print(self.postcodeTextbox.text())
        print(self.phoneNumberTextbox.text())
        print(self.emailTextbox.text())

        self.update()

    def update(self):
        print("Updating...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    
    sys.exit(app.exec_())