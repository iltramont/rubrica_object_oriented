# Classe che modella un utente di una rubrica telefonica

class Utente:
    def __init__(this, id: str, nome: str, cognome: str, indirizzo: str, cap: str,
                 citta: str, telefono: str, email: str):
        this.__id = str(id)
        this.__nome = str(nome)
        this.__cognome = str(cognome)
        this.__indirizzo = str(indirizzo)
        this.__cap = str(cap)
        this.__citta = str(citta)
        this.__telefono = str(telefono)
        this.__email = str(email)

    def getId(this):
        return this.__id

    def setId(this, id: str):
        this.__id = str(id)

    def getNome(this):
        return this.__nome

    def setNome(this, nome: str):
        this.__nome = str(nome)

    def getCognome(this):
        return this.__cognome

    def setCognome(this, cognome: str):
        this.__cognome = str(cognome)

    def getIndirizzo(this):
        return this.__indirizzo

    def setIndirizzo(this, indirizzo: str):
        this.__indirizzo = str(indirizzo)

    def getCAP(this):
        return this.__cap

    def setCAP(this, cap: str):
        this.__cap = str(cap)

    def getCitta(this):
        return this.__citta

    def setCitta(this, citta: str):
        this.__citta = str(citta)

    def getTelefono(this):
        return this.__telefono

    def setTelefono(this, telefono: str):
        this.__telefono = str(telefono)

    def getEmail(this):
        return this.__email

    def setEmail(this, email: str):
        this.__email = str(email)


    def trasformatiInStringa(this, colonne: list, t: int):     #t è la distanza minima tra i dati di un singolo utente
        s = this.__id.ljust(colonne[0]+t, " ") + this.__nome.ljust(colonne[1]+t, " ")\
            + this.__cognome.ljust(colonne[2]+t, " ") + this.__indirizzo.ljust(colonne[3]+t, " ") \
            + this.__cap.ljust(colonne[4]+t, " ") + this.__citta.ljust(colonne[5]+t, " ")\
            + this.__telefono.ljust(colonne[6]+t, " ") + this.__email.ljust(colonne[7]+t, " ")
        return s

    def __str__(this):
        return "       Id: " + this.__id +\
               "\n     Nome: " + this.__nome + "\n  Cognome: " + this.__cognome +\
               "\nIndirizzo: " + this.__indirizzo +\
               "\n      CAP: " + this.__cap + "\n    Città: " + this.__citta +\
               "\n Telefono: " + this.__telefono + "\n    Email: " + this.__email

    # Implementare il criterio di disuguaglianza tre livelli: nome - cognome - email
    def __lt__(this, other):
        risultato = this.__nome < other.__nome
        if this.__nome == other.__nome:
            risultato = this.__cognome < other.__cognome
            if this.__cognome == other.__cognome:
                risultato = this.__email < other.__email
        return risultato

    # Implementare il criterio di uguaglianza in base all'id
    def __eq__(this, other):
        return this.__id == other.__id


    # inverso di lt
    def __gt__(this, other):
        return other.__lt__(this)

    # inverso di eq
    def __ne__(this, other):
        return not this.__eq__(other)