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
            if risultato != "":
                risultato += ", "
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
        """
        restituisce la parola in input senza il punto interrogativo
        :param parola_punto_interrogativo: parola con un punto interrogativo al posto di una lettera
        :return: parola in input senza una lettera (c'era un punto interrogativo)
        """
        lista_parola = parola_punto_interrogativo.split("?")
        parola_pulita = ""
        for sezione in lista_parola:
            for lettera in sezione:
                parola_pulita += lettera
        return parola_pulita
    def cerca_parole_simili(self, parola_incompleta):
        """
        Data una parola che manca di una lettera restituisce una lista di parole simili
        :param parola_incompleta: parola senza una lettera
        :return: una lista di possibili parole che sostituiscano la parola in input
        """
        parole_accettabili = []
        for chiave in self.dizionarioParole.keys():
            if (len(chiave) - 1) == len(parola_incompleta):
                contatore = 0
                lettere_chiave = list(chiave)
                lettere_incompleta = list(parola_incompleta)
                for i in lettere_chiave:
                    for j in lettere_incompleta:
                        if i == j:
                            contatore += 1
                            lettere_incompleta.remove(j)
                            break
                if contatore == len(parola_incompleta):     ## se ho ogni lettera della parola imcompleta uguale ad almeno una lettera di una delle chiavi
                    parole_accettabili.append(chiave)
        return parole_accettabili
