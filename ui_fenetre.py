# Form implementation generated from reading ui file 'fenetre.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frameParams = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameParams.sizePolicy().hasHeightForWidth())
        self.frameParams.setSizePolicy(sizePolicy)
        self.frameParams.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameParams.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameParams.setObjectName("frameParams")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameParams)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frameParams)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.nbLettreRepetition = QtWidgets.QSpinBox(self.frameParams)
        self.nbLettreRepetition.setProperty("value", 4)
        self.nbLettreRepetition.setObjectName("nbLettreRepetition")
        self.verticalLayout_2.addWidget(self.nbLettreRepetition)
        self.label_2 = QtWidgets.QLabel(self.frameParams)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pourcentRepetition = QtWidgets.QSpinBox(self.frameParams)
        self.pourcentRepetition.setMaximum(100)
        self.pourcentRepetition.setProperty("value", 50)
        self.pourcentRepetition.setObjectName("pourcentRepetition")
        self.verticalLayout_2.addWidget(self.pourcentRepetition)
        self.label_3 = QtWidgets.QLabel(self.frameParams)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.distanceRepetition = QtWidgets.QSpinBox(self.frameParams)
        self.distanceRepetition.setMaximum(10000)
        self.distanceRepetition.setProperty("value", 200)
        self.distanceRepetition.setObjectName("distanceRepetition")
        self.verticalLayout_2.addWidget(self.distanceRepetition)
        self.label_4 = QtWidgets.QLabel(self.frameParams)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.distanceRepetitionLongue = QtWidgets.QSpinBox(self.frameParams)
        self.distanceRepetitionLongue.setMaximum(10000)
        self.distanceRepetitionLongue.setProperty("value", 1500)
        self.distanceRepetitionLongue.setObjectName("distanceRepetitionLongue")
        self.verticalLayout_2.addWidget(self.distanceRepetitionLongue)
        self.label_5 = QtWidgets.QLabel(self.frameParams)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.ignore = QtWidgets.QTextEdit(self.frameParams)
        self.ignore.setObjectName("ignore")
        self.verticalLayout_2.addWidget(self.ignore)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addWidget(self.frameParams, 1, 0, 1, 1)
        self.frameTexte = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameTexte.sizePolicy().hasHeightForWidth())
        self.frameTexte.setSizePolicy(sizePolicy)
        self.frameTexte.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameTexte.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameTexte.setObjectName("frameTexte")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameTexte)
        self.verticalLayout.setObjectName("verticalLayout")
        self.texte = QtWidgets.QPlainTextEdit(self.frameTexte)
        self.texte.setObjectName("texte")
        self.verticalLayout.addWidget(self.texte)
        self.gridLayout.addWidget(self.frameTexte, 1, 1, 1, 1)
        self.frameBoutons = QtWidgets.QFrame(self.centralwidget)
        self.frameBoutons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameBoutons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameBoutons.setObjectName("frameBoutons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameBoutons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.analyser = QtWidgets.QPushButton(self.frameBoutons)
        self.analyser.setObjectName("analyser")
        self.horizontalLayout.addWidget(self.analyser)
        self.gridLayout.addWidget(self.frameBoutons, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 20))
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
        self.label.setText(_translate("MainWindow", "Nombre de lettres communes:"))
        self.label_2.setText(_translate("MainWindow", "Pourcentage de comparaison:"))
        self.label_3.setText(_translate("MainWindow", "Distance max répétition proche:"))
        self.label_4.setText(_translate("MainWindow", "Distance max répétition longue:"))
        self.label_5.setText(_translate("MainWindow", "Mots à ignorer:"))
        self.ignore.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">je tu il elle on nous vous ils elles</p></body></html>"))
        self.analyser.setText(_translate("MainWindow", "Analyser"))