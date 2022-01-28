import csv
from app import db
from models import Etablissement, Inspection
from datetime import datetime, tzinfo

# Ajouter un établissement et son inspection
# e = Etablissement(nom = "Boulangerie Amry", adresse = "22 rue de Molsheim", cp = "67000", commune = "Strasbourg", siret = "123456789", activite = "boulangerie-patisserie", agrement = "987654321", longitude_latitude = "7.732310,48.577040", categorie_frais = "")
# db.session.add(e)
# i = Inspection(numero = "154861" , date= datetime.utcnow(), niveau_hygiene = "Satisfaisant", etablissement = e)
# db.session.add(i)
# db.session.commit()


with open('test_import.csv') as file:
    content = file.readlines()
    # header = content[:1]
    rows = content[1:]
    # print(header)
    # print(rows)
    for row in rows:
        print(row[0])
        # e = Etablissement(nom = row[0], siret = row[1],adresse = row[2], cp = row[3], commune = row[4], activite = row[7], agrement = row[9], longitude_latitude = row[10], categorie_frais = row[11])
        # db.session.add(e)
        # i = Inspection(numero = row[5], date = datetime.strptime(row[6], "%Y-%m-%dT%H:%M:%S%Z"), niveau_hygiene = row[8], etablissement = e)
        # db.session.add(i)

db.session.commit()