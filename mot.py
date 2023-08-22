class Mot:

    def __init__(self, mot):
        self.strPrint_ = mot
        self.strLow_ = mot.lower()
        self.proche_ = False
        self.loin_ = False

    def taille(self):
        return len(self.strPrint_)

    def strPrint(self):
        return self.strPrint_

    def strLow(self):
        return self.strLow_

    def proche(self):
        return self.proche_

    def loin(self):
        return self.loin_

    def match(self, mot, nbLettresCommunes, comparaison):
        if (len(self.strLow_) < nbLettresCommunes
                or len(mot.strLow()) < nbLettresCommunes):
            return False

        maxT = max(self.taille(), mot.taille())

        maxTrouve = 0
        for l in range(len(self.strLow_) - nbLettresCommunes + 1):
            nb = nbLettresCommunes
            ok = False
            substr = self.strLow_[l:l + nb]
            while mot.strLow().find(substr) >= 0 and len(
                    self.strLow_) >= l + nb:
                nb += 1
                ok = True
                substr = self.strLow_[l:l + nb + maxTrouve]
            maxTrouve = max(maxTrouve, nb - 1) if ok else maxTrouve

        if maxTrouve * 100. / maxT >= comparaison:
            return True

        maxTrouve = 0
        for l in range(mot.taille() - nbLettresCommunes + 1):
            nb = nbLettresCommunes
            ok = False
            substr = mot.strLow()[l:l + nb]
            while self.strLow_.find(substr) >= 0 and mot.taille() >= l + nb:
                nb += 1
                ok = True
                substr = mot.strLow()[l:l + nb]
            maxTrouve = max(maxTrouve, nb - 1) if ok else maxTrouve

        if maxTrouve * 100. / maxT >= comparaison:
            return True
        return False

    def marque(self, nbLettres, maxProche, maxLoin):
        if nbLettres <= maxProche:
            self.proche_ = True
        self.loin_ += 1

    def print(self):
        print(self.strPrint_ + " {} {}".format(self.proche_, self.loin_))
