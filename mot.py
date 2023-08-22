class Mot:

    def __init__(self, mot):
        self.str_ = mot
        self.strLow_ = mot.lower()
        self.proche_ = False
        self.loin_ = False

    def taille(self):
        return len(self.str_)

    def str(self):
        return self.str_

    def strLow(self):
        return self.strLow_

    def proche(self):
        return self.proche_

    def loin(self):
        return self.loin_

    def match(self, mot, nbLettresCommunes, comparaison):
        if (len(self.str_) < nbLettresCommunes
                or len(mot.str()) < nbLettresCommunes):
            return False

        maxT = max(self.taille(), mot.taille())

        maxTrouve = 0
        for l in range(len(self.str_) - nbLettresCommunes + 1):
            nb = nbLettresCommunes
            ok = False
            substr = self.str_[l:l + nb]
            while mot.str().find(substr) >= 0 and len(self.str_) >= l + nb:
                nb += 1
                ok = True
                substr = self.str_[l:l + nb + maxTrouve]
            maxTrouve = max(maxTrouve, nb - 1) if ok else maxTrouve

        if maxTrouve * 100. / maxT >= comparaison:
            return True

        maxTrouve = 0
        for l in range(mot.taille() - nbLettresCommunes + 1):
            nb = nbLettresCommunes
            ok = False
            substr = mot.str()[l:l + nb]
            while self.str_.find(substr) >= 0 and mot.taille() >= l + nb:
                nb += 1
                ok = True
                substr = mot.str()[l:l + nb]
            maxTrouve = max(maxTrouve, nb - 1) if ok else maxTrouve

        if maxTrouve * 100. / maxT >= comparaison:
            return True
        return False

    def marque(self, nbLettres, maxProche, maxLoin):
        if nbLettres <= maxProche:
            self.proche_ = True
        self.loin_ += 1

    def print(self):
        print(self.str_ + " {} {}".format(self.proche_, self.loin_))
