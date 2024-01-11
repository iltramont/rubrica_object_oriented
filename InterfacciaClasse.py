from RubricaClasse import Rubrica
from UtenteClasse import Utente

class Interfaccia:

    def __init__(this, rubrica: "Rubrica"):
        this.rubrica = rubrica

    """ come il comando input ma con la possibilità di impostare una lunghezza massima
        grazie al solito ciclo di controllo while
        viene anche evitato lutilizzo del carattere "|" """
    @staticmethod
    def inputControllato(messaggio: str, limite: int, carattere: str):
        a = input(messaggio)
        while len(a) > limite or carattere in a:
            if len(a) > limite:
                a = input("*****Troppi caratteri, riprovare\n-->")
            else:
                a = input("*****Il carattere: '" + carattere + "' non è consentito, riprova\n-->")
        return a

    """ Semplicemente aggiunge virgolette davanti e dietro a una stringa"""
    @staticmethod
    def virgoletta(stringa: str):
        return "\"" + stringa + "\""

    """ Metodo interattivo che serve a modificare un utente in maniera più volte, in più campi  """
    @staticmethod
    def modificaUtente(utente: "Utente"):
        valore = True
        while valore == True:
            print("\n--Digitare il comando corrispondente al campo da modificare\n"
                  "--Digitare 'f' per concludere la modifica\n"
                  "--Digitare 'u' per visualizzare il contatto")
            print("Nome: 1    Cognome: 2    Indirizzo: 3    CAP: 4    Città: 5    Telefono: 6    Email: 7")
            scelta = input("--> ").strip()
            if scelta == "f":
                valore = False
                print("--Modifica conclusa")
            elif scelta == "u":
                print(utente)
            else:
                while scelta not in "1234567" or scelta == "" or int(scelta) > 7:
                    scelta = input("*****Comando non valido, riprovare: ").strip()
                if scelta == "1":
                    print("--Stai per modificare " + Interfaccia.virgoletta(utente.getNome()))
                    campo = Interfaccia.inputControllato("--Nuovo nome: ", 20, "|").strip()
                    utente.setNome(campo)
                elif scelta == "2":
                    print("--Stai per modificare " + Interfaccia.virgoletta(utente.getCognome()))
                    campo = Interfaccia.inputControllato("--Nuovo Cognome: ", 20, "|").strip()
                    utente.setCognome(campo)
                elif scelta == "3":
                    print("--Stai per modificare " + Interfaccia.virgoletta(utente.getIndirizzo()))
                    campo = Interfaccia.inputControllato("--Nuovo indirizzo: ", 40, "|").strip()
                    utente.setIndirizzo(campo)
                elif scelta == "4":
                    print("--Stai per modificare " + Interfaccia.virgoletta(utente.getCAP()))
                    campo = Interfaccia.inputControllato("--Nuovo CAP: ", 10, "|").strip()
                    utente.setCAP(campo)
                elif scelta == "5":
                    print("--Stai per modificare " + Interfaccia.virgoletta(utente.getCitta()))
                    campo = Interfaccia.inputControllato("--Nuova città: ", 20, "|").strip()
                    utente.setCitta(campo)
                elif scelta == "6":
                    print("--Stai per modificare " + Interfaccia.virgoletta(utente.getTelefono()))
                    campo = Interfaccia.inputControllato("--Nuovo Telefono: ", 15, "|").strip()
                    utente.setTelefono(campo)
                else:
                    print("--Stai per modificare " + Interfaccia.virgoletta(utente.getEmail()))
                    campo = Interfaccia.inputControllato("--Nuova email: ", 40, "|").strip()
                    utente.setEmail(campo)

    """ Funzione interattiva che
        ritorna una lista di utenti (composta da uno o più utenti), se non trova nessuno restituisce None """
    def ricercaInRubrica(this):
        id = input("--Inserire ID oppure il nome del contatto: ").strip()
        a = this.rubrica.ricercaUtenteTramiteId(id)
        if type(a) != type(None):
            risultato = [a]  # è una lista con un singolo Utente
        else:
            nome = id
            cognome = input("--Inserire il cognome: ").strip()
            b = this.rubrica.ricercaUtentiTramiteNomeECognome(nome, cognome)
            risultato = b
        return risultato


    # Interfaccia del programma definita come metodo d'istanza, che viene richiamata di volta in volta dopo ogni scelta dell'utente.
    # Al suo interno, a seconda delle scelte dell'utente, verranno invocati i metodi corrispondenti
    # Si occupa del controllo sulla correttezza degli input dell'utilizzatore.
    def interfaccia(this):
        valore = True
        while valore == True:
            print("\n" + "-"*100 + "\nSegliere operazione:")
            print("--Visualizza rubrica: 1")
            print("----Ricerca contatti: 2")
            print("---Aggiungi contatto: 3")
            print("---Modifica contatto: 4")
            print("----Elimina contatti: 5")
            print("---------------Salva: 6")
            print("----------------Esci: 7")
            scelta = input("-->").strip()
            counter = 0
            while scelta not in "1234567" or scelta == "" or int(scelta) > 7:
                if scelta == "author":
                    print(
                        "Nome: Luca\nCognome: Tramonti\nMatricola: 4905197\nCorso di laurea: Matematica, c. Matematica")
                    scelta = input("-->").strip()
                elif scelta == "i love you 3000":
                    print("_" * 100 + "\n")
                    print(
                        "*******    *******  **     **    ******* *******  *******  **    |     **     **  *******  *       |")
                    print(
                        "   |       |     |  | ** ** |       |    |     |  |     |  | *   |     | ** ** |  |     |  |**     |")
                    print(
                        "   |       *******  |   *   |       |    |******  |     |  |  *  |     |   *   |  *******  |  ***  |")
                    print(
                        "   |       |     |  |       |       |    |  **    |     |  |   * |     |       |  |     |  |     **|")
                    print(
                        "*******    |     |  |       |    ******* |    **  *******  |    **     |       |  |     |  |       *")
                    print("\n" + "_" * 100)
                    scelta = input("-->").strip()
                elif counter == 5:
                    counter = counter +1
                    print("CE LA FAREMOOOOOHH")
                    scelta = input("-->")
                elif counter == 6:
                    counter = 0
                    print("Me sa de no")
                    scelta = input("-->")
                else:
                    counter = counter + 1
                    scelta = input("*****Comando non valido, riprova\n-->").strip()
            if scelta == "1":
                print("--Ecco la rubrica:\n")
                print(this.rubrica)
            if scelta == "2":
                print("")
                ricercati = this.ricercaInRubrica()
                if ricercati == []:
                    print("\n--Nessun contatto è stato trovato--")
                else:
                    #creo una Rubrica fittizia per poterla stampare facilmente con gli headers
                    print("--Ecco i contatti:\n")
                    print(Rubrica(ricercati))
            if scelta == "3":
                id = this.rubrica.generaId()
                if id == None:
                    print("*****La rubrica ha raggiunto il numero massimo di contatti*****\n"
                          "*****Eliminare contatti per proseguire proseguire*****")
                    continue
                print("--Inserire i dati del contatto")
                nome = Interfaccia.inputControllato("-------Nome: ", 20, "|").strip()
                cognome = Interfaccia.inputControllato("----Cognome: ", 20, "|").strip()
                a = this.rubrica.ricercaUtentiTramiteNomeECognome(nome, cognome)
                if a != []:
                    print("\n*****Attenzione, in rubrica sono già presenti contatti con lo stesso nome"
                          "\n--Ecco i contatti già presenti:\n")
                    print(Rubrica(a))
                    s = input("\n--Premere 'a' per annullare, 'c' per continuare \n-->").strip()
                    while s != "a" and s != "c":
                        s = input("*****Comando non valido, riprova\n-->").strip()
                    if s.strip() == "a":
                        continue
                indirizzo = Interfaccia.inputControllato("--Indirizzo: ", 40, "|").strip()
                cap = Interfaccia.inputControllato("--------CAP: ", 10, "|").strip()
                citta = Interfaccia.inputControllato("------Città: ", 20, "|").strip()
                telefono = Interfaccia.inputControllato("---Telefono: ", 15, "|").strip()
                email = Interfaccia.inputControllato("------Email: ", 40, "|").strip()
                nuovo_utente = Utente(id, nome, cognome, indirizzo, cap, citta, telefono, email)
                valore2 = True
                while valore2 == True:
                    print("\n--Stai per aggiungere il seguente contatto:\n\n" + str(nuovo_utente))
                    modifica = input("\n--Premere 'm' per modificarlo, 'a' per aggiungerlo in rubrica, 'e' per uscire"
                                     "\n-->").strip()
                    while modifica != "m" and modifica != "a" and modifica != "e":
                        modifica = input("*****Comando non valido, riprova\n-->").strip()
                    if modifica == "m":
                        Interfaccia.modificaUtente(nuovo_utente)
                    elif modifica == "e":
                        valore2 = False
                        print("--Operazione annullata")
                    else:
                        valore2 = False
                        this.rubrica.aggiungiModificaUtente(nuovo_utente)
            if scelta == "4":
                print("--Ricercare il contatto da modificare")
                ricercati = this.ricercaInRubrica()   #è una lista di Utenti
                if ricercati == []:
                    print("\n*****Nessun contatto è stato trovato*****")
                elif len(ricercati) == 1:
                    u = ricercati[0]
                    print("--Ecco il contatto che vuoi modificare:\n\n" + str(u))
                    # creo un utente fittizio in modo da poter tenere in  memoria il vecchio utente non modificato
                    utente_fittizio = Utente(str(u.getId()), u.getNome(), u.getCognome(), u.getIndirizzo(), u.getCAP(),
                                             u.getCitta(), u.getTelefono(), u.getEmail())
                    Interfaccia.modificaUtente(utente_fittizio)
                    valore3 = True
                    while valore3 == True:
                        print("\n--Contatto modificato:\n\n" + str(utente_fittizio))
                        modifica = input("\n--Premere 'm' per modificarlo ancora\n"
                                         "--Premere 'a' per annullare la modifica\n"
                                         "--qualsiasi altro tasto per confermare\n-->")
                        if modifica == "m":
                            Interfaccia.modificaUtente(utente_fittizio)
                        elif modifica == "a":
                            valore3 = False
                        else:
                            valore3 = False
                            this.rubrica.aggiungiModificaUtente(utente_fittizio)
                else:
                    # creo una Rubrica fittizia per poterla stampare facilmente con gli headers
                    rubrica_fittizia = Rubrica(ricercati)
                    print("\n--Ecco i contatti: ")
                    print(rubrica_fittizia)
                    id = input("\n--Digitare id corrispondente al contatto da modificare\n"
                               "--Peremere 'a' per annullare\n-->").strip()
                    u = rubrica_fittizia.ricercaUtenteTramiteId(id)
                    ###
                    while (type(u) == type(None)) and (id != "a"):
                        id = input("*****Comando non valido, riprovare\n-->").strip()
                        u = rubrica_fittizia.ricercaUtenteTramiteId(id)
                    if id == "a":
                        print("--Modifica annullata")
                    else:
                        #creo un utente fittizio in modo da poter tenere in  memoria il vecchio utente non modificato
                        utente_fittizio = Utente(str(u.getId()), u.getNome(), u.getCognome(), u.getIndirizzo(),
                                                 u.getCAP(), u.getCitta(), u.getTelefono(), u.getEmail())
                        Interfaccia.modificaUtente(utente_fittizio)
                        valore3 = True
                        while valore3 == True:
                            print("\n--Contatto modificato:\n\n"+str(utente_fittizio))
                            modifica = input("\n--Premere 'm' per modificarlo ancora\n"
                                             "--Premere 'a' per annullare la modifica\n"
                                             "--qualsiasi altro tasto per confermare\n-->")
                            if modifica == "m":
                                Interfaccia.modificaUtente(utente_fittizio)
                            elif modifica == "a":
                                valore3 = False
                            else:
                                valore3 = False
                                this.rubrica.aggiungiModificaUtente(utente_fittizio)
            if scelta == "5":
                print("--Cercare il contatto da eliminare")
                ricercati = this.ricercaInRubrica()
                if ricercati == []:
                    print("\n*****Nessun contatto è stato trovato*****")
                elif len(ricercati) == 1:
                    u = ricercati[0]
                    print("--Il seguente contatto sta per essere eliminato:\n\n " + str(u))
                    conferma = input("\n--Conferma y/n\n-->").strip()
                    while conferma != "y" and conferma != "n":
                        conferma = input("*****Comando non valido, riprovare\n-->")
                    if conferma == "y":
                        this.rubrica.cancellaUtente(u.getId())
                        print("--Contatto eliminato")
                    else:
                        print("--Modifica annullata")
                else:
                    #tutti i ricercati hanno lo stesso nome e cognome
                    nome = ricercati[0].getNome()
                    cognome = ricercati[0].getCognome()
                    print("--I seguenti contatti stanno per essere eliminati:\n")
                    rubrica_fittizia = Rubrica(ricercati)
                    print(rubrica_fittizia)
                    conferma = input("\n--Premere 'y' per confermare\n--Premere 'a' per annullare\n"
                                     "--Digitare Id per eliminare solo il contatto corrispondente\n-->").strip()
                    x = rubrica_fittizia.ricercaUtenteTramiteId(conferma)
                    while conferma != "y" and conferma != "a" and type(x) == type(None):
                        conferma = input("*****Comando non valido, riprovare\n-->")
                        x = rubrica_fittizia.ricercaUtenteTramiteId(conferma)
                    if conferma == "y":
                        this.rubrica.cancellaUtenti(nome, cognome)
                        print("--Contatti eliminati")
                    elif conferma == "a":
                        print("--Modifica annullata")
                    else:
                        this.rubrica.cancellaUtente(conferma)
                        print("--Contatto eliminato")
            if scelta == "6":
                filepath = this.rubrica.getFilePath()
                this.rubrica.salvaRubrica(filepath)
                print("--Rubrica salvata in " + filepath)
            if scelta == "7":
                salvataggio = input("--Premere 's' per salvare, premere 'n' per uscire senza salvare\n-->").strip()
                while salvataggio != "s" and salvataggio != "n":
                    salvataggio = input("*****Comando non valido, riprovare\n-->").strip()
                if salvataggio == "s":
                    filepath = this.rubrica.getFilePath()
                    this.rubrica.salvaRubrica(filepath)
                    print("--Rubrica salvata in " + filepath)
                valore = False
                print("\n--Chiusura Programma")


# Funzione di avvio del programma
def main():
    print("Da qui puoi gestire la tua rubrica\n")
    r = Rubrica.leggiRubrica("rubrica_oo.txt")
    i = Interfaccia(r)
    i.interfaccia()

if __name__ == "__main__":
     main()