import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Inserire numero: ")

    # Add input control here!
    try:
        txtIn = int(txtIn)
        if int(txtIn) == 1:
            print("Quale parola devo aggiungere?")
            txtIn_str = input("Inserire parola aliena e parola italiana separati da uno spazio: ")
            txtIn_str = txtIn_str.lower()
            if t.controlla_aggiunta_parole(txtIn_str) == True:
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
                print(parola_italiana)
            else:
                print("Parola non valida")
        elif int(txtIn) == 3:
            pass
        elif int(txtIn) == 4:
            print(t.stampa_dizionario())
        elif int(txtIn) == 5:
            break
        else:
            print("Comando non valido")
    except ValueError:
        print("Errore di input")