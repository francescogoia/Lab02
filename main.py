import translator as tr

t = tr.Translator()

contatore_run = 0
while(True):
    t.printMenu()
    if contatore_run == 0:
        t.loadDictionary("dictionary.txt")
        contatore_run += 1
    txtIn = input("Inserire numero: ")
    # Add input control here!
    try:
        txtIn = int(txtIn)
        if int(txtIn) == 1:
            print("Quale parola devo aggiungere?")
            txtIn_str = input("Inserire parola aliena e parola italiana separati da uno spazio: ")
            txtIn_str = txtIn_str.lower()
            if t.controlla_aggiunta_parole(txtIn_str):
                t.handleAdd(txtIn_str)
                print("Aggiunta!")
            else:
                print("Parole non valide")
                pass
        elif int(txtIn) == 2:
            print("Quale parola devo cercare?")
            txtIn_str = input("Inserire parola aliena: ")
            txtIn_str = txtIn_str.lower()
            if t.controlla_parola(txtIn_str):
                parola_italiana = t.handleTranslate(txtIn_str)
                print("La traduzione di '", txtIn_str, "' è: ", parola_italiana)
            else:
                print("Parola non valida")
                pass
        elif int(txtIn) == 3:
            print("Quale parola devo cercare (con wildcard)?")
            txtIn_str = input("Inserire parola aliena: ")
            txtIn_str = txtIn_str.lower()
            if t.controlla_parola_wildcard(txtIn_str):
                print("accettata")
                parola_italiana = t.handleWildCard(txtIn_str)
                print(print("La traduzione di '", txtIn_str, "' è: ", parola_italiana))

            pass
        elif int(txtIn) == 4:
            print(t.stampa_dizionario())
        elif int(txtIn) == 5:
            break
        else:
            print("Comando non valido")
    except ValueError:
        print("Errore di input")