# partie 1 :
"""
personne = {'nom': 'Mélanie', "age": 25, 'taille': 1.60}

print(personne['nom'])
personne['poste'] = "Développeur"

achat = ("Chocolat", "beurre", "fromage")
personne["Liste Course"] = achat

print(personne)
"""

# partie 2 :
# personnes = [
#     ("Mélanie", 18, 1.3),
#     ("Paul", 56, 1.2),
#     ("Jack", 25, 1.8),
#     ("Amandine", 26, 1.6),
# ]
#
#
# def afficher_contenu(nom, people):
#     for i in people:
#         if i[0] == nom:
#             print(i)
#     return None
#
#
# afficher_contenu("Jack", personnes)

personnes = {
    'Mélanie': (18, 1.3),
    'Paul': (56, 1.2),
    'Jack': (25, 1.8),
    'Amandine': (26, 1.6)
}


infos = personnes.get('fe')
print(infos)
