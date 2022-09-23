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
		self.texte_ = Texte()

	def clicAnalyser(self):
		document = self.texte.document()
		format = QTextCharFormat()
		format.setBackground(Qt.GlobalColor.white)
		cursor = QTextCursor(document)
		cursor.select(QTextCursor.SelectionType.Document)
		cursor.setCharFormat(format)
		cursor.clearSelection()
		cursor.movePosition(QTextCursor.MoveOperation.Start)

		self.texte_.analyse(document,
							self.nbLettreRepetition.value(),
							self.pourcentRepetition.value(),
							self.distanceRepetition.value(),
							self.distanceRepetitionLongue.value())

		mots = self.texte_.mots()
		index = 0

		while not cursor.atEnd():
			cursor.select(QTextCursor.SelectionType.WordUnderCursor)
			mot = cursor.selectedText()
			if mot != mots[index].str():
				print("Erreur, décalage: {} != {}".format(mot, mots[index].str()))

			if mots[index].proche():
				format = QTextCharFormat()
				format.setBackground(Qt.GlobalColor.yellow)
				cursor.setCharFormat(format)
			elif mots[index].loin():
				format = QTextCharFormat()
				format.setBackground(Qt.GlobalColor.green)
				cursor.setCharFormat(format)

			cursor.movePosition(QTextCursor.MoveOperation.NextWord)
			index += 1


