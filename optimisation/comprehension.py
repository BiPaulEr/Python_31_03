noms = ["Alice", "Bob", "Charlie"]

liste2 = [prenom.upper() for prenom in noms if len(prenom) > 3]
print(liste2) #['ALICE', 'CHARLIE']