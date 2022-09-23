
from mot import Mot

class Texte():
	def __init__(self):
		self.mots_ = list()

	def analyse(self,
				txt,
				nbLettresCommunes = 4,
				comparaison = 50,
				maxProche = 150,
				maxLoin = 1500,
				ignore = list()):
		self.mots_ = list()
		mots = txt.split()
		for m in mots:
			self.mots_.append(Mot(m))

		for index in range(len(self.mots_)):
			pos = 1
			nbLettres = 0
			while index + pos < len(self.mots_) and nbLettres < maxLoin:
				if self.mots_[index + pos] not in ignore and self.mots_[index + pos].match(self.mots_[index],
																						   nbLettresCommunes,
																						   comparaison):
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
