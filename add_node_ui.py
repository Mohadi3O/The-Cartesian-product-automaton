# Form implementation generated from reading ui file 'c:\Users\omar\Documents\Python Scripts\meps2\add_node.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 264)
        MainWindow.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.name.setText("")
        self.name.setObjectName("name")
        self.horizontalLayout_2.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.c = QtWidgets.QComboBox(self.centralwidget)
        self.c.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.c.setObjectName("c")
        self.horizontalLayout_3.addWidget(self.c)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 255);")
        self.submit.setObjectName("submit")
        self.verticalLayout.addWidget(self.submit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 344, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "add node "))
        self.label_2.setText(_translate("MainWindow", "name :"))
        self.label_3.setText(_translate("MainWindow", "Type  :"))
        self.submit.setText(_translate("MainWindow", "Submit"))