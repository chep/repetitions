from PyQt6.QtWidgets import QMainWindow

from ui_fenetre import Ui_MainWindow
from texte import Texte

class Fenetre(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(Fenetre, self).__init__()
		self.setupUi(self)
		self.analyser.clicked.connect(self.clicAnalyser)
		self.texte_ = Texte()

	def clicAnalyser(self):
		self.texte_.analyse(self.texte.toPlainText(),
							self.nbLettreRepetition.value(),
							self.pourcentRepetition.value(),
							self.distanceRepetition.value(),
							self.distanceRepetitionLongue.value())
		texte = self.texte.toPlainText()
		motsBruts = texte.split()
		mots = self.texte_.mots()

		position = 0
		for index in range(len(mots)):
			position += texte[position:].find(motsBruts[index])
			if mots[index].proche():
				texte = texte[:position] + '<span style=\"background-color:#ffff00;\" >' + motsBruts[index] + "</span>" + texte[position+len(motsBruts[index]):]
			elif mots[index].loin():
				texte = texte[:position] + '<span style=\"background-color:#00ff00;\" >' + motsBruts[index] + "</span>" + texte[position+len(motsBruts[index]):]
			position += len(motsBruts[index])

		self.texte.clear()
		self.texte.appendHtml(texte)

