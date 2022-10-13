
from mot import Mot
from PyQt6.QtGui import QTextCursor

class Texte():
	def __init__(self):
		self.mots_ = list()

	def analyse(self,
				doc,
				nbLettresCommunes = 4,
				comparaison = 50,
				maxProche = 150,
				maxLoin = 1500,
				ignore = list()):
		cursor = QTextCursor(doc)
		self.mots_ = list()
		while not cursor.atEnd():
			cursor.select(QTextCursor.SelectionType.WordUnderCursor)
			self.mots_.append(Mot(cursor.selectedText()))
			cursor.movePosition(QTextCursor.MoveOperation.NextWord)

		for index in range(len(self.mots_)):
			if self.mots_[index].str() not in ignore:
				pos = 1
				nbLettres = 0
				while index + pos < len(self.mots_) and nbLettres < maxLoin:
					if (self.mots_[index + pos].str() not in ignore
						    and self.mots_[index + pos].match(self.mots_[index],
															  nbLettresCommunes,
															  comparaison)):
						self.mots_[index + pos].marque(nbLettres,
													   maxProche,
													   maxLoin)
						self.mots_[index].marque(nbLettres,
												 maxProche,
												 maxLoin)
					nbLettres += self.mots_[index + pos].taille()
					pos += 1

	def mots(self):
		return self.mots_

	def cherche(self,
				mot,
				doc,
				nbLettresCommunes = 4,
				comparaison = 50,
				maxProche = 150,
				maxLoin = 1500):
		cursor = QTextCursor(doc)
		self.mots_ = list()
		while not cursor.atEnd():
			cursor.select(QTextCursor.SelectionType.WordUnderCursor)
			self.mots_.append(Mot(cursor.selectedText()))
			cursor.movePosition(QTextCursor.MoveOperation.NextWord)
		for index in range(len(self.mots_)):
			if self.mots_[index].str() == mot:
				pos = 1
				nbLettres = 0
				while index + pos < len(self.mots_) and nbLettres < maxLoin:
					if (self.mots_[index + pos].match(self.mots_[index],
													  nbLettresCommunes,
													  comparaison)):
						self.mots_[index + pos].marque(nbLettres,
													   maxProche,
													   maxLoin)
						self.mots_[index].marque(nbLettres,
												 maxProche,
												 maxLoin)
					nbLettres += self.mots_[index + pos].taille()
					pos += 1
