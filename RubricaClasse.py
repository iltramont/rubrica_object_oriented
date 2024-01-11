# Classe che modella una rubrica telefonica con una serie di utenti

from UtenteClasse import Utente

class Rubrica:
    headers = ["--Id--", "--Nome--", "--Cognome--", "--Indirizzo--", "--CAP--",
               "--Città--", "--Telefono--", "--E-mail--"]

    def __init__(this, utenti: list):
        this.__utenti = utenti
        this.__filepath = None  # può tornare utile questo attributo per l'interfaccia


    def getUtenti(this):
        return this.__utenti

    def setUtenti(this, utenti: list):
        this.__utenti = utenti

    def getFilePath(this):
        return this.__filepath

    def setFilepath(this, filepath: str):
        this.__filepath = filepath

    # Salva la Rubrica con la sua lista di Utenti
    # su un file specificato, scrivendo un Utente per riga,
    # i cui attributi vengono separati dal carattere pipe (|)
    def salvaRubrica(this, filepath: str):
        f = open(filepath, "w")
        for i in range(0, len(this.__utenti)):
            u = this.__utenti[i]
            # Trasforma ciascun Utente in una stringa concatenando i suoi attributi separati da una pipe e scrivila sul file
            stringa = u.getId()+"|"+u.getNome()+"|"+u.getCognome()+"|"+u.getIndirizzo()+"|"+u.getCAP()+"|"+u.getCitta()+"|"+u.getTelefono()+"|"+u.getEmail()
            if(i < len(this.__utenti)-1):
                stringa = stringa + "\n"
            f.write(stringa)
        f.close()

    # Legge un file testuale specificato che rappresenta una rubrica
    # e restituisce in output un oggetto Rubrica che comprende una lista di Utenti.
    @staticmethod
    def leggiRubrica(filepath: str) -> "Rubrica":
        f = open(filepath, "r")
        utenti = []
        lines = f.readlines()
        for l in lines:
            # Leggi la riga e trasformala in un utente per poi aggiungerla alla rubrica
            s = l.replace("\n", "").split("|")
            utente = Utente(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7])
            utenti.append(utente)
        f.close()
        rubrica = Rubrica(utenti)
        rubrica.setFilepath(filepath) # può tornare utile all'interfaccia per salvare la Rubrica...
        return rubrica

    #genera l' id minore possibile tra quelli non presenti in rubrica
    #da U000 a U999
    def generaId(this):
        risultato = None
        insieme_id = set()
        for utente in this.__utenti:
            insieme_id.add(utente.getId())
        for k in range(0, 1000, 1):
            if k < 10:
                i = "U00" + str(k)
            elif k > 9 and k <100:
                i = "U0" + str(k)
            else:
                i = "U" + str(k)
            #appena trova un id valido si ferma
            if i not in insieme_id:
                risultato = i
                break
        return risultato

    #fornisce una lista di interi rappresentante la larghezza massima di ogni tipo di dato degli utenti in rubrica
    def larghezzaColonne(this) -> list:
        #inizializzo gli insiemi con la larghezza degli headers
        l_nomi = {len(Rubrica.headers[1])}
        l_cognomi = {len(Rubrica.headers[2])}
        l_indirizzo = {len(Rubrica.headers[3])}
        l_CAP = {len(Rubrica.headers[4])}
        l_citta = {len(Rubrica.headers[5])}
        l_telefono = {len(Rubrica.headers[6])}
        l_email = {len(Rubrica.headers[7])}
        for utente in this.__utenti:
            l_nomi.add(len(utente.getNome()))
            l_cognomi.add(len(utente.getCognome()))
            l_indirizzo.add(len(utente.getIndirizzo()))
            l_CAP.add(len(utente.getCAP()))
            l_citta.add(len(utente.getCitta()))
            l_telefono.add(len(utente.getTelefono()))
            l_email.add(len(utente.getEmail()))
        larghezze = [6, max(l_nomi), max(l_cognomi), max(l_indirizzo),         #6 è la lunghezza della stringa "--id--"
                     max(l_CAP), max(l_citta), max(l_telefono), max(l_email)]
        return larghezze

    # Fornisce una rappresentazione in formato stringa della Rubrica con i suoi Utenti e gli headers
    #la scelta della spaziatura la si sceglie da qui, io ho messo 4
    def __str__(this):
        #ordino la rubrica prima di iniziare
        this.__utenti.sort()
        v = 4
        c = this.larghezzaColonne()
        lista_stringhe = []
        #trasformo gli headers in una stringa con la giusta spaziatura
        headers_corretti = []
        for i in range(0,8):
            headers_corretti.append(Rubrica.headers[i].ljust(c[i] + v))
        lista_stringhe.append("".join(headers_corretti))
        for utente in this.__utenti:
            lista_stringhe.append(utente.trasformatiInStringa(c, v))
        stringa = "\n".join(lista_stringhe)
        return stringa

    # Cerca nella Rubrica Utenti con il nome e cognome passati in input (a prescindere da maiuscole/minuscole),
    # e se li trova restituisce una lista di Utenti trovati,
    # altrimenti restituisce una lista vuota
    def ricercaUtentiTramiteNomeECognome(this, nome: str, cognome: str) -> list:
        risultato = list()
        for u in this.__utenti:
            #strip viene lasciato fare all'interfaccia
            if nome.lower() == u.getNome().lower() and cognome.lower() == u.getCognome().lower():
                risultato.append(u)
        return risultato

    # Cerca nella Rubrica un Utente con l'id passato in input
    # e se lo trova restituisce l'Utente in output,
    # altrimenti restituisce un valore None.
    def ricercaUtenteTramiteId(this, id: str) -> "Utente":
        risultato = None
        for u in this.__utenti:
            if id == u.getId():
                risultato = u
                break
        return risultato

    # Prende in input un Utente,
    # verifica se è già presente un Utente nella Rubrica con lo stesso id
    # e se esiste sovrascrive l'Utente esistente con tutti i suoi dati,
    # altrimenti lo aggiunge alla Rubrica.
    def aggiungiModificaUtente(this, utente: "Utente"):
        valore = True
        for u in this.__utenti:
            if u == utente:
                this.__utenti.remove(u)
                this.__utenti.append(utente)
                valore = False
                break
        if valore == True:
            this.__utenti.append(utente)

    # Cerca un Utente nella Rubrica con l'id specificato
    # e se lo trova lo cancella dalla Rubrica. Restituisce l'eventuale Utente che era presente.
    def cancellaUtente(this, id: str) -> "Utente":
        risultato = None
        for utente in this.__utenti:
            if utente.getId() == id:
                this.__utenti.remove(utente)
                risultato = utente
                break
        return risultato

    # Cerca Utenti nella Rubrica con il nome e cognome specificati (a prescindere da maiuscole/minuscole),
    # e se li trova li cancella dalla Rubrica. Restituisce la lista degli eventuali Utenti cancellati.
    def cancellaUtenti(this, nome: str, cognome: str) -> list:
        risultato = []
        for u in this.__utenti:
            if u.getNome().lower() == nome.lower() and u.getCognome().lower() == cognome.lower():
                risultato.append(u)
        for r in risultato:
            this.__utenti.remove(r)
        return risultato
