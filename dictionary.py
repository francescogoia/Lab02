class Dictionary:
    def __init__(self):
        self.dizionarioParole = {}

    def __repr__(self):
        stringa = ""
        for key in self.dizionarioParole.keys():
            stringa += key + " = " + self.dizionarioParole[key] + "\n"
        return stringa

    def addWord(self, parola_aliena, parole_italiane, presente):
        if presente == False:
            self.dizionarioParole.update({parola_aliena : parole_italiane})
        else:
            self.dizionarioParole[parola_aliena].append(parole_italiane)

    def translate(self, parola_aliena):
        try:
            parola_italiana = self.dizionarioParole[parola_aliena]
            return parola_italiana
        except KeyError:
            print("Parola non presente nel dizionario")

    def translateWordWildCard(self):
        pass

