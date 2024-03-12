class Dictionary:
    def __init__(self):
        self.dizionarioParole = {}

    def __repr__(self):
        stringa = ""
        for key in self.dizionarioParole.keys():
            stringa += key + " = " + self.translate(key) + "\n"
        return stringa

    def addWord(self, parola_aliena, parole_italiane, presente):
        if presente == False:
            self.dizionarioParole.update({parola_aliena : parole_italiane})
        else:
            for parola in parole_italiane:
                self.dizionarioParole[parola_aliena].append(parola)

    def translate(self, parola_aliena):
        try:
            parole_italiane = self.dizionarioParole[parola_aliena]
            return self.restituisci_traduzione(parole_italiane)
        except KeyError:
            print("Parola non presente nel dizionario")

    def translateWordWildCard(self, parola_aliena_punto_interrogativo):
        parola_pulita_incompleta = self.restituisci_parola_wildcard(parola_aliena_punto_interrogativo)
        parole_accettabili = self.cerca_parole_simili(parola_pulita_incompleta)
        risultato = ""
        for parola_aliena in parole_accettabili:
            risultato += self.translate(parola_aliena)
        return risultato

    def restituisci_traduzione(self, lista_parole_italiane):
        risultato = ""
        for parola in lista_parole_italiane:
            if risultato != "":
                risultato += ", "
            risultato += parola
        return risultato
    def restituisci_parola_wildcard(self, parola_punto_interrogativo):
        lista_parola = parola_punto_interrogativo.split("?")
        parola_pulita = ""
        for sezione in lista_parola:
            for lettera in sezione:
                parola_pulita += lettera
        return parola_pulita
    def cerca_parole_simili(self, parola_incompleta):
        parole_accettabili = []
        for chiave in self.dizionarioParole.keys():
            if (len(chiave) - 1) == len(parola_incompleta):
                contatore = 0
                for i in range(len(chiave)):
                    if i < len(parola_incompleta):





                        if chiave[i] == parola_incompleta[i]:
                            contatore += 1
                    else:                                               ## ultima lettera
                        if chiave[i] == parola_incompleta[len(parola_incompleta) - 1]:
                            contatore += 1
                if contatore == len(parola_incompleta) - 1:
                    parole_accettabili.append(chiave)
        return parole_accettabili
