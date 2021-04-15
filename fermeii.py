import os
from PyQt5 import QtCore, QtGui, QtWidgets


class sorry_form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 209)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 50, 421, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.closebtn = QtWidgets.QPushButton(Form)
        self.closebtn.setGeometry(QtCore.QRect(240, 170, 93, 28))
        self.closebtn.setObjectName("closebtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sayonara!!"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sorry we could not provide you with your choice today. We hope to see you soon again. Have a good day!</span></p></body></html>"))
        self.closebtn.setText(_translate("Form", "Close"))

        self.closebtn.clicked.connect(self.close)

    def close(a,b):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sorry_form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
