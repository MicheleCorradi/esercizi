import sqlite3

conn = sqlite3.connect('immobili.db')
curs = conn.cursor()

try:
    curs.execute("DROP table immobile")
    curs.execute("DROP table catalogo")
except:
    pass

curs.execute("CREATE table immobile (riferimento char(20),proprietario char(20),indirizzo char(30),prezzo int(15),citta char(20),catalogo char(20))")


class Immobile():
    def __init__(self, riferimento, proprietario, indirizzo, prezzo, citta):
        self.riferimento = riferimento
        self.prezzo = prezzo
        self.citta = citta
        self.indirizzo = indirizzo
        self.proprietario = proprietario 

    def modifica_prezzo(self, prezzo_nuovo):
        self.prezzo = prezzo_nuovo
        print ("Hai modificato il prezzo")
    
    def stampa_info_immobile(self):
        print("L'immobile in %s di %s, %s costa %d" % (self.citta, self.proprietario, self.indirizzo, self.prezzo))

class Catalogo():
    def __init__(self, nome,cursore):
        self.nome = nome
        self.file = self.nome + ".p" ## Crea il nome per il file (.p estensione per file pickle)
        self.immobili = [] ## O lista()
        self.cursore = cursore

    def aggiungi_immobile(self, immobile):
        self.immobili.append(immobile)
        row = (immobile.riferimento, immobile.proprietario, immobile.indirizzo,immobile.prezzo, immobile.citta, self.nome)
        self.cursore.execute("INSERT INTO immobile values(?,?,?,?,?,?)",row)
        print("Immobile aggiunto correttamente!")

    def elimina_immobile(self, immobile):
        if immobile in self.immobili:
            self.immobili.remove(immobile)
            self.cursore.execute("DELETE FROM immobile WHERE riferimento = ?",(immobile.riferimento,))
            print("Immobile rimosso dalla lista")
        else:
            print("Immobile non presente in lista")

    def stampa_catalogo(self):
        for immobile in self.immobili:
            immobile.stampa_info_immobile()
        print("dal database:")
        self.cursore.execute("SELECT * FROM immobile")
        for row in self.cursore.fetchall():
            print(row)
    
    def cerca_immobile(self, proprietario):
        print("Il proprietario selezionato possiede i seguenti immobili:")
        for immobile in self.immobili:
            if immobile.proprietario == proprietario:
                immobile.stampa_info_immobile()
        print("dal database:")
        self.cursore.execute("SELECT * FROM immobile WHERE proprietario = ?",(immobile.proprietario, ))
        for row in self.cursore.fetchall():
            print(row)


Catalogo1 = Catalogo("Catalogo1",curs)

casa1 = Immobile("1", "Marco", "Via Roma", 500, "Grosseto")
casa2 = Immobile("2", "Marco", "Via Ciao", 400, "Grosseto")
casa3 = Immobile("3", "Marco", "Via Ciao", 700, "Grosseto")


Catalogo1.aggiungi_immobile(casa1)
Catalogo1.aggiungi_immobile(casa2)
Catalogo1.aggiungi_immobile(casa3)

Catalogo1.stampa_catalogo()
Catalogo1.cerca_immobile("Marco")

conn.commit()
conn.close()