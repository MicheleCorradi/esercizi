import pickle

class Immobile():
    def __init__(self, id, proprietario, indirizzo, prezzo, citta):
        self.id = id
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
    def __init__(self, nome):
        self.nome = nome
        self.file = self.nome + ".p" ## Crea il nome per il file (.p estensione per file pickle)
        self.immobili = [] ## O lista()

    def aggiungi_immobile(self, immobile):
        self.immobili.append(immobile)
        print("Immobile aggiunto correttamente!")

    def elimina_immobile(self, immobile):
        if immobile in self.immobili:
            self.immobili.remove(immobile)
            print("Immobile rimosso dalla lista")
        else:
            print("Immobile non presente in lista")

    def stampa_catalogo(self):
        for immobile in self.immobili:
            immobile.stampa_info_immobile()
    
    def cerca_immobile(self, proprietario):
        print("Il proprietario selezionato possiede i seguenti immobili:")
        for immobile in self.immobili:
            if immobile.proprietario == proprietario:
                immobile.stampa_info_immobile()

    def leggi(self):
        with open(self.file, 'rb') as file:
            self.immobili = pickle.load(file)

    def salva(self):
        with open(self.file, 'wb') as file:
            pickle.dump(self.immobili, file)
        print("Salvataggio Completato")
    

## La parte dentro gli apici sotto va prima mandata per salvare i dati
    
"""

Catalogo1 = Catalogo("Catalogo1")

casa1 = Immobile("1", "Marco", "Via Roma", 500, "Grosseto")
casa2 = Immobile("2", "Marco", "Via Ciao", 400, "Grosseto")
casa3 = Immobile("3", "Marco", "Via Ciao", 700, "Grosseto")


casa1.stampa_info_immobile()
casa1.modifica_prezzo(600)
casa1.stampa_info_immobile()

Catalogo1.aggiungi_immobile(casa1)
Catalogo1.aggiungi_immobile(casa2)
Catalogo1.aggiungi_immobile(casa3)

Catalogo1.stampa_catalogo()

Catalogo1.elimina_immobile(casa1)

Catalogo1.stampa_catalogo()

Catalogo1.cerca_immobile("Marco")

Catalogo1.salva()
"""

Catalogo_Palle = Catalogo("Catalogo1")

Catalogo_Palle.leggi()

Catalogo_Palle.stampa_catalogo()