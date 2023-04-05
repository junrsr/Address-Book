from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys
import mysql.connector

class EnterDetails(QMainWindow):
    def __init__(self):
        super(EnterDetails, self).__init__()
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
        conn = mysql.connector.connect(host="localhost", database="addressBook", user="root", password="sGs-w1llncc")
        cursor = conn.cursor()

        print(type(self.fNameTextbox.text()))
        
        
        try:
            cursor.execute(f"""insert into people(firstName, lastName, address, city, postcode, phoneNumber, email) values(
                '{self.fNameTextbox.text()}',
                '{self.lNameTextbox.text()}',
                '{self.addressTextbox.text()}',
                '{self.cityTextbox.text()}',
                '{self.postcodeTextbox.text()}',
                '{self.phoneNumberTextbox.text()}',
                '{self.emailTextbox.text()}')""")
            print("Successfully added to the database")
            conn.commit()
            
        except:
            print("Unable to add to the database")
            conn.rollback()
        
        finally:
            cursor.close()
            conn.close()
        self.update()

    def update(self):
        print("Updating...")


class ViewDetails(QTableWidget):

    def __init__(self):
        QTableWidget.__init__(self, self.getNoOfEntries(), 7)
        self.setGeometry(0, 0, 620, 300)
        self.setWindowTitle("Address Book")
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.show()
    
    def getNoOfEntries(self):
        self.conn = mysql.connector.connect(host="localhost", database="addressBook", user="root", password="sGs-w1llncc")
        self.cursor = self.conn.cursor()

        self.cursor.execute("select firstName, lastName, address, city, postcode, phoneNumber, email from people order by lastName")
        self.rows = self.cursor.fetchall()

        return len(self.rows)
    
    def setData(self):
        horHeaders = ["First Name", "Last Name", "Address", "City", "Postcode", "Phone Number", "Email Address"]

        for x in range(len(self.rows)):
            for y in range(len(self.rows[x])):
                newItem = QTableWidgetItem(self.rows[x][y])
                self.setItem(x, y, newItem)

        self.setHorizontalHeaderLabels(horHeaders)
        self.verticalHeader().setVisible(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #win = EnterDetails()
    win = ViewDetails()

    sys.exit(app.exec_())
    
#TODO ADD FUNCTIONALITY TO SWITCH BETWEEN PAGES (plus button to add entry? switch back to database by default?)