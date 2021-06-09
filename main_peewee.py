import peewee

db = peewee.SqliteDatabase("immobili_peewee.db")

class CatalogoImmobili(peewee.Model):
    riferimento = peewee.CharField()
    proprietario = peewee.CharField()
    indirizzo = peewee.CharField()
    citta = peewee.CharField()
    prezzo = peewee.IntegerField()
    catalogo = peewee.CharField()

    class Meta:
        database = db
        db_table = 'immobili'

CatalogoImmobili.create_table(CatalogoImmobili)

casa1 = CatalogoImmobili.create(riferimento = "1a", proprietario = "nicola losito", indirizzo =  "via roma 2", citta = "grosseto", prezzo = 50000, catalogo = "generale")
casa2 = CatalogoImmobili.create(riferimento = "2a", proprietario = "mario rossi", indirizzo =  "via dossi 5", citta = "pisa", prezzo = 150000, catalogo = "generale")

casa1.save()
casa2.save()

immobili = CatalogoImmobili.select()

for immobile in immobili:
    print(immobile.riferimento, immobile.proprietario)
