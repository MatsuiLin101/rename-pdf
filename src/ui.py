from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rename(object):
    def setupUi(self, Rename):
        Rename.setObjectName("Rename")
        Rename.resize(600, 450)
        self.centralwidget = QtWidgets.QWidget(Rename)
        self.centralwidget.setObjectName("centralwidget")
        self.text_area = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_area.setGeometry(QtCore.QRect(0, 110, 600, 340))
        self.text_area.setObjectName("text_area")
        self.btn_folder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_folder.setGeometry(QtCore.QRect(0, 5, 120, 50))
        self.btn_folder.setObjectName("btn_folder")
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setEnabled(False)
        self.btn_confirm.setGeometry(QtCore.QRect(480, 55, 120, 50))
        self.btn_confirm.setObjectName("btn_confirm")
        self.text_folder = QtWidgets.QLabel(self.centralwidget)
        self.text_folder.setGeometry(QtCore.QRect(120, 5, 250, 50))
        self.text_folder.setObjectName("text_folder")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setEnabled(False)
        self.btn_clear.setGeometry(QtCore.QRect(0, 55, 120, 50))
        self.btn_clear.setObjectName("btn_clear")
        Rename.setCentralWidget(self.centralwidget)

        self.retranslateUi(Rename)
        QtCore.QMetaObject.connectSlotsByName(Rename)

    def retranslateUi(self, Rename):
        _translate = QtCore.QCoreApplication.translate
        Rename.setWindowTitle(_translate("Rename", "MainWindow"))
        self.text_area.setHtml(_translate("Rename", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">初始化完成...</p></body></html>"))
        self.btn_folder.setText(_translate("Rename", "選擇資料夾"))
        self.btn_confirm.setText(_translate("Rename", "重新命名"))
        self.text_folder.setText(_translate("Rename", "尚未選擇"))
        self.btn_clear.setText(_translate("Rename", "重置"))
