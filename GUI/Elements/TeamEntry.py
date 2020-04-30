# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeamEntry.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(789, 633)
        self.teamBoxWidget = QtWidgets.QWidget(Dialog)
        self.teamBoxWidget.setGeometry(QtCore.QRect(240, 190, 191, 103))
        self.teamBoxWidget.setObjectName("teamBoxWidget")
        self.teamBox = QtWidgets.QVBoxLayout(self.teamBoxWidget)
        self.teamBox.setContentsMargins(0, 0, 0, 0)
        self.teamBox.setObjectName("teamBox")
        
        self.teamNumberLine = QtWidgets.QLineEdit(self.teamBoxWidget)
        self.teamNumberLine.setMaximumSize(QtCore.QSize(16777215, 20))
        self.teamNumberLine.setText("")
        self.teamNumberLine.setAlignment(QtCore.Qt.AlignCenter)
        self.teamNumberLine.setObjectName("teamNumberLine")
        self.teamBox.addWidget(self.teamNumberLine)
        
        self.speedLine = QtWidgets.QLineEdit(self.teamBoxWidget)
        self.speedLine.setAlignment(QtCore.Qt.AlignCenter)
        self.speedLine.setObjectName("speedLine")
        self.teamBox.addWidget(self.speedLine)
    
    self.shootingTimeLine = QtWidgets.QLineEdit(self.teamBoxWidget)
        self.shootingTimeLine.setAlignment(QtCore.Qt.AlignCenter)
        self.shootingTimeLine.setObjectName("shootingTimeLine")
        self.teamBox.addWidget(self.shootingTimeLine)

        self.sendButton = QtWidgets.QPushButton(self.teamBoxWidget)
        self.sendButton.setMaximumSize(QtCore.QSize(16777215, 23))
        self.sendButton.setObjectName("sendButton")
        self.teamBox.addWidget(self.sendButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.teamNumberLine.setPlaceholderText(_translate("Dialog", "Enter Team Number"))
        self.speedLine.setPlaceholderText(_translate("Dialog", "Average Speed During Autonomous"))
        self.shootingTimeLine.setPlaceholderText(_translate("Dialog", "Shooting Time"))
        self.sendButton.setText(_translate("Dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
