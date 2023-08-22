from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QTextCursor, QTextBlockFormat, QTextCharFormat
from PyQt6.QtCore import Qt

from ui_fenetre import Ui_MainWindow
from texte import Texte


class Fenetre(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Fenetre, self).__init__()
        self.setupUi(self)
        self.analyser.clicked.connect(self.clicAnalyser)
        self.rechercher.clicked.connect(self.clicRechercher)
        self.texte_ = Texte()

    def clear(self):
        document = self.texte.document()
        format = QTextCharFormat()
        format.setBackground(Qt.GlobalColor.white)
        cursor = QTextCursor(document)
        cursor.select(QTextCursor.SelectionType.Document)
        cursor.setCharFormat(format)

    def clicAnalyser(self):
        self.clear()
        document = self.texte.document()

        self.texte_.analyse(document, self.nbLettreRepetition.value(),
                            self.pourcentRepetition.value(),
                            self.distanceRepetition.value(),
                            self.distanceRepetitionLongue.value(),
                            self.ignore.toPlainText().split())
        self.maj()

    def maj(self):
        document = self.texte.document()
        cursor = QTextCursor(document)
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        mots = self.texte_.mots()
        index = 0

        while not cursor.atEnd():
            cursor.select(QTextCursor.SelectionType.WordUnderCursor)
            mot = cursor.selectedText()
            if mot != mots[index].str():
                print("Erreur, décalage: {} != {}".format(
                    mot, mots[index].str()))

            if mots[index].proche():
                format = QTextCharFormat()
                format.setBackground(Qt.GlobalColor.yellow)
                cursor.setCharFormat(format)
            elif mots[index].loin() >= self.occurrenceRepetitionLongue.value():
                format = QTextCharFormat()
                format.setBackground(Qt.GlobalColor.green)
                cursor.setCharFormat(format)

            cursor.movePosition(QTextCursor.MoveOperation.NextWord)
            index += 1

    def clicRechercher(self):
        self.clear()
        document = self.texte.document()
        self.texte_.cherche(self.motCherche.text(), document,
                            self.nbLettreRepetition.value(),
                            self.pourcentRepetition.value(),
                            self.distanceRepetition.value(),
                            self.distanceRepetitionLongue.value())
        self.maj()
