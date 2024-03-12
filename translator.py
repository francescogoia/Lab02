import dictionary as d
class Translator:

    def __init__(self):
        self.dizionarioParole = d.Dictionary()

    def printMenu(self):
        print("----------------")
        print("Translator Alien-Italian")
        print("----------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4- Stampa tutto il dizionario")
        print("5. Exit")
        pass

    def loadDictionary(self, dict):
        fileDizionario = open(dict, 'r', encoding='utf-8')
        listaTraduzioni = fileDizionario.readlines()
        fileDizionario.close()
        for i in listaTraduzioni:
            i = i.strip()
            parola_aliena = i.split()[0]
            parola_italiana = i.split()[1]
            parole_italiane = []
            parole_italiane.append(parola_italiana)
            self.dizionarioParole.addWord(parola_aliena, parole_italiane, False)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        lista = entry.split()
        parola_aliena = lista[0]
        parole_italiane = []
        for i in range(len(lista)):
            if i != 0:
                parole_italiane.append(lista[i])
        if self.parola_gia_salvata(parola_aliena) == False:
            self.dizionarioParole.addWord(parola_aliena, parole_italiane, False)
        else:
            self.dizionarioParole.addWord(parola_aliena, parole_italiane, True)
        pass

    def handleTranslate(self, query):
        return self.dizionarioParole.translate(query)


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.dizionarioParole.translateWordWildCard(query)

    def stampa_dizionario(self):
        return self.dizionarioParole.__repr__()

    def controlla_aggiunta_parole(self, stringa):
        entry = stringa.split()
        if len(entry) >= 2:
            for parola in entry:
                if self.controlla_parola(parola) == False:
                    return False
        return True
    def controlla_parola(self, parola):
        for lettera in parola:
            if lettera < "a" or lettera > "z":
                return False
        return True
    def controlla_parola_wildcard(self, parola):
        lista_parola = parola.split("?")
        for sezione in lista_parola:
            if len(lista_parola) > 2 :
                return False
            for lettera in sezione:
                if lettera < "a" or lettera > "z":
                    return False
        return True
    def parola_gia_salvata(self, parola_aliena):
        for parola in self.dizionarioParole.dizionarioParole.keys():
            if parola_aliena == parola:
                return True
        return False
