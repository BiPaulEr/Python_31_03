prenoms = ["Paul", "Ernest", "Martin", "p"]
noms = ["Dupont", "Lefebvre", "Aigouyi"]
nations = ["fr", "fr", "fr"]
#[(0, ('Paul', 'Dupont', 'fr')), (1, ('Ernest', 'Lefebvre', 'fr')), (2, ('Martin', 'Aigouyi', 'fr'))]

for index, (prenom, nom, nation) in enumerate(zip(prenoms, noms, nations)):
    prenoms[index] = prenom.upper()
    noms[index] = nom.upper()
    nations[index] = nation.upper()

print(prenoms, noms, nations)
#['PAUL', 'ERNEST', 'MARTIN', 'p'] ['DUPONT', 'LEFEBVRE', 'AIGOUYI'] ['FR', 'FR', 'FR'] 
print("end")
