import socket
import pickle
import sys
from datetime import datetime
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets


current = None
view = None
transaction = None
total = 0

# message to be sent to cleanly disconnect from server
DISCONNECTOR = "!DISCONNECT"
# fetch this machine's ip address
SERVER = socket.gethostbyname(socket.gethostname())
# port selection
PORT = 9000
ADDR = (SERVER, PORT)
# format to be used for transmission
FORMAT = 'utf-8'
# max size of messages
BYTES = 1024

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
# bind address and port to socket

# class for welcome message
client.connect(ADDR)
class Ui_welcome(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(712, 461)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(200, 340, 331, 23))
        # self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.thevendingmachine = QtWidgets.QLabel(Form)
        self.thevendingmachine.setGeometry(QtCore.QRect(180, 40, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        self.thevendingmachine.setFont(font)
        self.thevendingmachine.setObjectName("thevendingmachine")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(150, 120, 421, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 390, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.thevendingmachine.setText(_translate("Form", "The Vending Machine"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Welcome to THE VENDING MACHINE</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Hopefully we have the snack you wish to snack on.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Instructions:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To use THE VENDING MACHINE, in the keypad please use the format: </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#f90000;\">ID#Quantity</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "ENTER"))
        self.pushButton.clicked.connect(self.next)

    # fill progess bar when enter button is clicked
    def next(self):
        for i in range(101):
            time.sleep(0.05)
            self.progressBar.setValue(i)
        time.sleep(1)

# class for card payment
class Ui_card(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(356, 372)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(160, 80, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 320, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 250, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 130, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 190, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 250, 151, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Card payment"))
        self.comboBox.setItemText(0, _translate("Form", "MCB"))
        self.comboBox.setItemText(1, _translate("Form", "American Express"))
        self.comboBox.setItemText(2, _translate("Form", "SBM"))
        self.label.setText(_translate("Form", "Bank"))
        self.label_2.setText(_translate("Form", "Card number:"))
        self.label_3.setText(_translate("Form", "CVV number:"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.label_4.setText(_translate("Form", "Enter credit card details"))
        self.label_5.setText(_translate("Form", "Expiry Date:"))
        self.pushButton.clicked.connect(self.preuceed)


    def preuceed(self):
        # check if all fields have been filled
        if self.lineEdit_4.text() and self.lineEdit_2.text() and self.lineEdit_3.text():
            from datetime import datetime
            global transaction
            # append to transaction dictionary card details
            transaction['card'] = [self.comboBox.currentText(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text()]
            # display goodbye message
            os.system('python goodbye.py')
            # append to transactions file the card details
            with open("transactions.txt", 'a') as f:
                f.write(datetime.now().strftime("%H:%M:%S"))
                f.write(f"  -- Card -- Rs{total}")
                f.write('\n')
                for key in transaction:
                    string = ''
                    for element in transaction[key]:
                        string += f"{element}@"
                    f.write(string)
                    f.write('--')
                f.write('\n\n')
            # send disconnect message to server
            client.send(DISCONNECTOR.encode(FORMAT))
            # close client
            sys.exit()

        else:
            # notify user that not all fields have been filled
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("You have not filled all required fields")
            x = msg.exec()

# class for the cas payment
class Ui_cash(object):
    def setupUi(self, Form):
        global total
        Form.setObjectName("Form")
        Form.resize(582, 281)
        self.amt_due = QtWidgets.QLabel(Form)
        self.amt_due.setGeometry(QtCore.QRect(50, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.amt_due.setFont(font)
        self.amt_due.setObjectName("amt_due")
        self.cash_back = QtWidgets.QLabel(Form)
        self.cash_back.setGeometry(QtCore.QRect(50, 95, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.cash_back.setFont(font)
        self.cash_back.setObjectName("cash_back")
        self.rs5 = QtWidgets.QPushButton(Form)
        self.rs5.setGeometry(QtCore.QRect(90, 150, 61, 51))
        self.rs5.setObjectName("rs5")
        self.rs10 = QtWidgets.QPushButton(Form)
        self.rs10.setGeometry(QtCore.QRect(160, 150, 61, 51))
        self.rs10.setObjectName("rs10")
        self.rs20 = QtWidgets.QPushButton(Form)
        self.rs20.setGeometry(QtCore.QRect(230, 150, 61, 51))
        self.rs20.setObjectName("rs20")
        self.rs25 = QtWidgets.QPushButton(Form)
        self.rs25.setGeometry(QtCore.QRect(300, 150, 101, 51))
        self.rs25.setObjectName("rs25")
        self.rs50 = QtWidgets.QPushButton(Form)
        self.rs50.setGeometry(QtCore.QRect(410, 150, 101, 51))
        self.rs50.setObjectName("rs50")
        self.amt = QtWidgets.QLabel(Form)
        self.amt.setGeometry(QtCore.QRect(210, 30, 81, 16))
        self.amt.setObjectName("amt")
        self.back = QtWidgets.QLabel(Form)
        self.back.setGeometry(QtCore.QRect(210, 100, 81, 16))
        self.back.setObjectName("back")
        self.current = QtWidgets.QLabel(Form)
        self.current.setGeometry(QtCore.QRect(210, 65, 81, 16))
        self.current.setObjectName("current")
        self.current_balance = QtWidgets.QLabel(Form)
        self.current_balance.setGeometry(QtCore.QRect(50, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.current_balance.setFont(font)
        self.current_balance.setObjectName("current_balance")
        self.proceed = QtWidgets.QPushButton(Form)
        self.proceed.setGeometry(QtCore.QRect(240, 220, 101, 51))
        self.proceed.setObjectName("proceed")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.inpt = 0
        self.flag = False
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cash payment"))
        self.proceed.setText(_translate("Form", "Next"))
        self.amt_due.setText(_translate("Form", "Amount due:"))
        self.cash_back.setText(_translate("Form", "Cash back:"))
        self.rs5.setText(_translate("Form", "5"))
        self.rs10.setText(_translate("Form", "10"))
        self.rs20.setText(_translate("Form", "20"))
        self.rs25.setText(_translate("Form", "25"))
        self.rs50.setText(_translate("Form", "50"))
        self.amt.setText(_translate("Form", f"Rs {total}"))
        self.back.setText(_translate("Form", "N/A"))
        self.current.setText(_translate("Form", f"{self.inpt}"))
        self.current_balance.setText(_translate("Form", "Current balance:"))

        # link buttons
        self.rs5.clicked.connect(self.add5)
        self.rs10.clicked.connect(self.add10)
        self.rs20.clicked.connect(self.add20)
        self.rs25.clicked.connect(self.add25)
        self.rs50.clicked.connect(self.add50)
        self.proceed.clicked.connect(self.preuceed)

    def preuceed(self):
        # check whether enough money has been input by the user before going forward with the transaction
        if self.flag == True:
            os.system('python goodbye.py')
            global transaction
            # write transaction to transactions file
            with open("transactions.txt", 'a') as f:
                f.write(datetime.now().strftime("%H:%M:%S"))
                f.write(f"  -- Cash -- Rs{total}")
                f.write('\n')
                for key in transaction:
                    string = ''
                    for element in transaction[key]:
                        string += f"{element}@"
                    f.write(string)
                    f.write('--')
                f.write('\n\n')
            # send disconnector message to server
            client.send(DISCONNECTOR.encode(FORMAT))
            # close interface
            sys.exit()

        # notify user that not enough money has been entered
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("You have not input enough money")
            x = msg.exec()

# set of functions that make the buttons work
    def add5(self):
        self.inpt = self.inpt + 5
        self.current.setText(f"Rs {self.inpt}")
        self.returnamt()

    def add10(self):
        self.inpt = self.inpt + 10
        self.current.setText(f"Rs {self.inpt}")
        self.returnamt()

    def add20(self):
        self.inpt = self.inpt + 20
        self.current.setText(f"Rs {self.inpt}")
        self.returnamt()

    def add25(self):
        self.inpt = self.inpt + 25
        self.current.setText(f"Rs {self.inpt}")
        self.returnamt()

    def add50(self):
        self.inpt = self.inpt + 50
        self.current.setText(f"Rs {self.inpt}")
        self.returnamt()

    def returnamt(self):
        if total - self.inpt <= 0:
            self.back.setText(f"Rs {self.inpt - total}")
            self.flag = True

# class for the initial vending machine
class Ui_Vending(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(606, 879)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 571, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("a.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 240, 81, 121))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 370, 81, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-image: url(\"c.png\");")
        self.pushButton.setStyleSheet("background-image: url(\"b.png\");")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "THE VENDING MACHINE"))
        self.pushButton.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", ""))
        self.pushButton.clicked.connect(self.fetch_stock)
        self.pushButton_2.clicked.connect(self.launch_keypad)

    # logic behind the visualisation of the stock currently in the database
    def fetch_stock(self):
        import matplotlib.pyplot as plt

        # send request for stock information from server
        client.send("stock".encode(FORMAT))
        stock = pickle.loads(client.recv(BYTES))
        # list comprehension to create 2 separate lists for the data to be represented in the barchart
        names = [x[0] for x in stock]
        stck = [x[1] for x in stock]

        # barchart specifics
        plt.bar(names, stck, color='blue', width=0.35)
        plt.xlabel("Item")
        plt.ylabel("Quantity in stock")
        plt.title("Current stock in vending machine")

        plt.show()

    # method to display the keypad
    def launch_keypad(self):
        # self.fetch_stock()
        view.show()

# class for menu that appeaers after each input in the keypad
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 173)
        self.another = QtWidgets.QPushButton(Form)
        self.another.setGeometry(QtCore.QRect(50, 90, 151, 51))
        self.another.setObjectName("another")
        self.payout = QtWidgets.QPushButton(Form)
        self.payout.setGeometry(QtCore.QRect(210, 90, 151, 51))
        self.payout.setObjectName("payout")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(370, 90, 151, 51))
        self.cancel.setObjectName("cancel")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 20, 201, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "What next?"))
        self.another.setText(_translate("Form", "Add another item"))
        self.payout.setText(_translate("Form", "Finish and pay"))
        self.cancel.setText(_translate("Form", "Cancel order"))
        self.label.setText(_translate("Form", "What do you want to do next?"))
        self.another.clicked.connect(self.anada)
        self.payout.clicked.connect(self.payoot)
        self.cancel.clicked.connect(self.nvm)

    # close menu to allow user to use keypad again
    def anada(self,b):
        current.close()

    # proceed to payout
    def payoot(self,b):
        current.close()

        # send signal to server requesting for information
        client.send("payout".encode(FORMAT))
        receipt = pickle.loads(client.recv(BYTES))
        # create receipt
        for key in receipt:
            receipt[key].append(str(receipt[key][1]*receipt[key][2]))

        # app = QtWidgets.QApplication(sys.argv)
        self.rcpt = QtWidgets.QWidget()
        self.ui = Ui_receipt()
        self.ui.setupUi(self.rcpt, receipt)
        self.rcpt.show()
        global transaction
        transaction = receipt

    # close everything and display message of apology
    def nvm(self,b):
        os.system('python fermeii.py')
        client.send(DISCONNECTOR.encode(FORMAT))
        sys.exit()

# Create a subclass of QMainWindow to setup the keypad's GUI
class KeypadUi(QMainWindow):
    """Keypad's View (GUI)."""
    def __init__(self):
        self.receipt = []
        """View initializer."""
        super().__init__()
        self.setWindowTitle('Keypad')
        self.setFixedSize(350, 450)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(45)
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'1': (0, 0),
                   '2': (0, 1),
                   '3': (0, 2),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '7': (2, 0),
                   '8': (2, 1),
                   '9': (2, 2),
                   'CLEAR': (3, 0),
                   '#': (3, 1),
                   'ENTER': (3, 2),
                  }
        # Create the buttons and add them to the grid layout

        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(80, 80)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        #Get display's text
        return self.display.text()

    def clearDisplay(self):
        #Clear the display
        self.setDisplayText('')

# using partial from functools for reduced amounts of code
from functools import partial
#Keypad Controller class
class KeypadCtrl:
    def __init__(self, view):
        #Controller initializer
        self._view = view
        # Connect signals and slots
        self._connectSignals()
    def _buildExpression(self, btnText):
        #Build expression
        self.expression = self._view.displayText() + btnText
        self._view.setDisplayText(self.expression)

    def _connectSignals(self):
        #Connect signals and slots
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'ENTER', 'CLEAR'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        self._view.buttons['CLEAR'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['ENTER'].clicked.connect(self._creatercpt)


    def _creatercpt(self):
        receipt = []
        # send what is currently displayed
        client.send(self.expression.encode(FORMAT))

        response = self.validate()
        # check what has been sent back and act accordingly
        if response =='Invalid ID' or response == 'Please use format: ID#Quantity' or response == 'Item not available in desired quantity' or response == 'Please use format: ID#Quantity':
            self.show_popup(response)
        elif response == 'restocked successfully':
            self.show_popup(response, "RESTOCK!!")
            sys.exit()
        self._view.clearDisplay()
        self.read()

    # method for displaying error message
    def show_popup(self, response, type = "Error"):
        msg = QMessageBox()
        msg.setWindowTitle(type)
        msg.setText(response)
        x = msg.exec()

    def validate(self):
        return client.recv(1024).decode(FORMAT)

    def read(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

        global current
        current = self.Form

# class for the receipt
class Ui_receipt(object):
    def setupUi(self, Form, dct):
        self.dct = dct
        Form.setObjectName("Form")
        Form.resize(358, 518)
        self.card = QtWidgets.QPushButton(Form)
        self.card.setGeometry(QtCore.QRect(180, 440, 101, 51))
        self.card.setObjectName("card")
        self.card = QtWidgets.QPushButton(Form)
        self.card.setGeometry(QtCore.QRect(180, 440, 101, 51))
        self.card.setObjectName("card")
        self.cash = QtWidgets.QPushButton(Form)
        self.cash.setGeometry(QtCore.QRect(60, 440, 101, 51))
        self.cash.setObjectName("cash")
        self.a1 = QtWidgets.QLabel(Form)
        self.a1.setGeometry(QtCore.QRect(30, 140, 55, 16))
        self.a1.setObjectName("a1")
        self.a2 = QtWidgets.QLabel(Form)
        self.a2.setGeometry(QtCore.QRect(100, 140, 55, 16))
        self.a2.setObjectName("a2")
        self.a3 = QtWidgets.QLabel(Form)
        self.a3.setGeometry(QtCore.QRect(180, 140, 55, 16))
        self.a3.setObjectName("a3")
        self.a4 = QtWidgets.QLabel(Form)
        self.a4.setGeometry(QtCore.QRect(270, 140, 55, 16))
        self.a4.setObjectName("a4")
        self.b2 = QtWidgets.QLabel(Form)
        self.b2.setGeometry(QtCore.QRect(100, 160, 55, 16))
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QLabel(Form)
        self.b3.setGeometry(QtCore.QRect(180, 160, 55, 16))
        self.b3.setObjectName("b3")
        self.b1 = QtWidgets.QLabel(Form)
        self.b1.setGeometry(QtCore.QRect(30, 160, 55, 16))
        self.b1.setObjectName("b1")
        self.b4 = QtWidgets.QLabel(Form)
        self.b4.setGeometry(QtCore.QRect(270, 160, 55, 16))
        self.b4.setObjectName("b4")
        self.c2 = QtWidgets.QLabel(Form)
        self.c2.setGeometry(QtCore.QRect(100, 180, 55, 16))
        self.c2.setObjectName("c2")
        self.d1 = QtWidgets.QLabel(Form)
        self.d1.setGeometry(QtCore.QRect(30, 200, 55, 16))
        self.d1.setObjectName("d1")
        self.c3 = QtWidgets.QLabel(Form)
        self.c3.setGeometry(QtCore.QRect(180, 180, 55, 16))
        self.c3.setObjectName("c3")
        self.d3 = QtWidgets.QLabel(Form)
        self.d3.setGeometry(QtCore.QRect(180, 200, 55, 16))
        self.d3.setObjectName("d3")
        self.d4 = QtWidgets.QLabel(Form)
        self.d4.setGeometry(QtCore.QRect(270, 200, 55, 16))
        self.d4.setObjectName("d4")
        self.c1 = QtWidgets.QLabel(Form)
        self.c1.setGeometry(QtCore.QRect(30, 180, 55, 16))
        self.c1.setObjectName("c1")
        self.c4 = QtWidgets.QLabel(Form)
        self.c4.setGeometry(QtCore.QRect(270, 180, 55, 16))
        self.c4.setObjectName("c4")
        self.d2 = QtWidgets.QLabel(Form)
        self.d2.setGeometry(QtCore.QRect(100, 200, 55, 16))
        self.d2.setObjectName("d2")
        self.e2 = QtWidgets.QLabel(Form)
        self.e2.setGeometry(QtCore.QRect(100, 220, 55, 16))
        self.e2.setObjectName("e2")
        self.f1 = QtWidgets.QLabel(Form)
        self.f1.setGeometry(QtCore.QRect(30, 240, 55, 16))
        self.f1.setObjectName("f1")
        self.g2 = QtWidgets.QLabel(Form)
        self.g2.setGeometry(QtCore.QRect(100, 260, 55, 16))
        self.g2.setObjectName("g2")
        self.e3 = QtWidgets.QLabel(Form)
        self.e3.setGeometry(QtCore.QRect(180, 220, 55, 16))
        self.e3.setObjectName("e3")
        self.h1 = QtWidgets.QLabel(Form)
        self.h1.setGeometry(QtCore.QRect(30, 280, 55, 16))
        self.h1.setObjectName("h1")
        self.f3 = QtWidgets.QLabel(Form)
        self.f3.setGeometry(QtCore.QRect(180, 240, 55, 16))
        self.f3.setObjectName("f3")
        self.g1 = QtWidgets.QLabel(Form)
        self.g1.setGeometry(QtCore.QRect(30, 260, 55, 16))
        self.g1.setObjectName("g1")
        self.h2 = QtWidgets.QLabel(Form)
        self.h2.setGeometry(QtCore.QRect(100, 280, 55, 16))
        self.h2.setObjectName("h2")
        self.g3 = QtWidgets.QLabel(Form)
        self.g3.setGeometry(QtCore.QRect(180, 260, 55, 16))
        self.g3.setObjectName("g3")
        self.h3 = QtWidgets.QLabel(Form)
        self.h3.setGeometry(QtCore.QRect(180, 280, 55, 16))
        self.h3.setObjectName("h3")
        self.f4 = QtWidgets.QLabel(Form)
        self.f4.setGeometry(QtCore.QRect(270, 240, 55, 16))
        self.f4.setObjectName("f4")
        self.e4 = QtWidgets.QLabel(Form)
        self.e4.setGeometry(QtCore.QRect(270, 220, 55, 16))
        self.e4.setObjectName("e4")
        self.e1 = QtWidgets.QLabel(Form)
        self.e1.setGeometry(QtCore.QRect(30, 220, 55, 16))
        self.e1.setObjectName("e1")
        self.f2 = QtWidgets.QLabel(Form)
        self.f2.setGeometry(QtCore.QRect(100, 240, 55, 16))
        self.f2.setObjectName("f2")
        self.h4 = QtWidgets.QLabel(Form)
        self.h4.setGeometry(QtCore.QRect(270, 280, 55, 16))
        self.h4.setObjectName("h4")
        self.g4 = QtWidgets.QLabel(Form)
        self.g4.setGeometry(QtCore.QRect(270, 260, 55, 16))
        self.g4.setObjectName("g4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 330, 301, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 110, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(100, 110, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(170, 110, 100, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(280, 110, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.i4 = QtWidgets.QLabel(Form)
        self.i4.setGeometry(QtCore.QRect(270, 300, 55, 16))
        self.i4.setObjectName("i4")
        self.i1 = QtWidgets.QLabel(Form)
        self.i1.setGeometry(QtCore.QRect(30, 300, 55, 16))
        self.i1.setObjectName("i1")
        self.i2 = QtWidgets.QLabel(Form)
        self.i2.setGeometry(QtCore.QRect(100, 300, 55, 16))
        self.i2.setObjectName("i2")
        self.i3 = QtWidgets.QLabel(Form)
        self.i3.setGeometry(QtCore.QRect(180, 300, 55, 16))
        self.i3.setObjectName("i3")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(80, 350, 181, 22))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_37 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.sumtotal = QtWidgets.QLabel(self.splitter_2)
        self.sumtotal.setObjectName("sumtotal")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(50, 380, 261, 41))

        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.inpt = 0
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Your receipt"))
        self.cash.setText(_translate("Form", "Cash"))
        self.card.setText(_translate("Form", "Card"))
        self.label_10.setText(_translate("Form", "Payment method:"))
        self.cash.clicked.connect(self.cashh)
        self.card.clicked.connect(self.cardd)

        # store number of elements in dictionary
        num = len(self.dct)
        # create a list of keys
        keys = [x for x in self.dct.keys()]
        # buffer list to store values
        jaja = []
        # check how many elements bought and alter appropriate label with appropriate data
        if num > 0:
            self.a1.setText(_translate("Form", self.dct[keys[0]][0]))
            self.a2.setText(_translate("Form", f"{self.dct[keys[0]][1]}"))
            self.a3.setText(_translate("Form", f"{self.dct[keys[0]][2]}"))
            jaja.append(self.dct[keys[0]][3])
            self.a4.setText(_translate("Form", f"{jaja[0]}"))
        if num > 1:
            self.b1.setText(_translate("Form", f"{self.dct[keys[1]][0]}"))
            self.b2.setText(_translate("Form", f"{self.dct[keys[1]][1]}"))
            self.b3.setText(_translate("Form", f"{self.dct[keys[1]][2]}"))
            jaja.append(self.dct[keys[1]][3])
            self.b4.setText(_translate("Form", f"{jaja[1]}"))
        if num > 2:
            self.c1.setText(_translate("Form", f"{self.dct[keys[2]][0]}"))
            self.c2.setText(_translate("Form", f"{self.dct[keys[2]][1]}"))
            self.c3.setText(_translate("Form", f"{self.dct[keys[2]][2]}"))
            jaja.append(self.dct[keys[0]][3])
            self.c4.setText(_translate("Form", f"{jaja[2]}"))
        if num > 3:
            self.d1.setText(_translate("Form", f"{self.dct[keys[3]][0]}"))
            self.d2.setText(_translate("Form", f"{self.dct[keys[3]][1]}"))
            self.d3.setText(_translate("Form", f"{self.dct[keys[3]][2]}"))
            jaja.append(self.dct[keys[3]][3])
            self.d4.setText(_translate("Form", f"{jaja[3]}"))
        if num > 4:
            self.e1.setText(_translate("Form", f"{self.dct[keys[4]][0]}"))
            self.e2.setText(_translate("Form", f"{self.dct[keys[4]][1]}"))
            self.e3.setText(_translate("Form", f"{self.dct[keys[4]][2]}"))
            jaja.append(self.dct[keys[4]][3])
            self.e4.setText(_translate("Form", f"{jaja[4]}"))
        if num > 5:
            self.f1.setText(_translate("Form", f"{self.dct[keys[5]][0]}"))
            self.f2.setText(_translate("Form", f"{self.dct[keys[5]][1]}"))
            self.f3.setText(_translate("Form", f"{self.dct[keys[5]][2]}"))
            jaja.append(self.dct[keys[5]][3])
            self.f4.setText(_translate("Form", f"{jaja[5]}"))
        if num > 6:
            self.g1.setText(_translate("Form", f"{self.dct[keys[6]][0]}"))
            self.g2.setText(_translate("Form", f"{self.dct[keys[6]][1]}"))
            self.g3.setText(_translate("Form", f"{self.dct[keys[6]][2]}"))
            jaja.append(self.dct[keys[6]][3])
            self.g4.setText(_translate("Form", f"{jaja[6]}"))
        if num > 7:
            self.h1.setText(_translate("Form", f"{self.dct[keys[7]][0]}"))
            self.h2.setText(_translate("Form", f"{self.dct[keys[7]][1]}"))
            self.h3.setText(_translate("Form", f"{self.dct[keys[7]][2]}"))
            jaja.append(self.dct[keys[7]][3])
            self.h4.setText(_translate("Form", f"{jaja[7]}"))

        if num > 8:
            self.i1.setText(_translate("Form", f"{self.dct[keys[8]][0]}"))
            self.i2.setText(_translate("Form", f"{self.dct[keys[8]][1]}"))
            self.i3.setText(_translate("Form", f"{self.dct[keys[8]][2]}"))
            jaja.append(self.dct[keys[8]][3])
            self.i4.setText(_translate("Form", f"{jaja[8]}"))

        # calculate total for this user
        global total
        for val in jaja:
            total += int(val)

        self.label_5.setText(_translate("Form", "YOUR RECEIPT"))
        self.label_6.setText(_translate("Form", "Item"))
        self.label_7.setText(_translate("Form", "Price"))
        self.label_8.setText(_translate("Form", "Quantity"))
        self.label_9.setText(_translate("Form", "Total"))
        self.label_37.setText(_translate("Form", "Sum Total:"))
        self.sumtotal.setText(_translate("Form", str(total)))

    # display cash ui
    def cashh(self):
        self.cashhh = QtWidgets.QWidget()
        self.ui = Ui_cash()
        self.ui.setupUi(self.cashhh)
        self.cashhh.show()

    # display card ui
    def cardd(self):
        self.card = QtWidgets.QWidget()
        self.ui = Ui_card()
        self.ui.setupUi(self.card)
        self.card.show()


# Client code
def main():
    global view
    # Create an instance of QApplication
    Keypad = QApplication(sys.argv)
    # Show the keypad's GUI
    view = KeypadUi()
    # Create instances of the model and the controller
    KeypadCtrl(view=view)
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Vending()
    ui.setupUi(Form)
    Form.show()
    # Execute the keypad's main loop
    sys.exit(Keypad.exec_())

    view.close()

if __name__ == '__main__':
    os.system('python welcome.py')
    main()
