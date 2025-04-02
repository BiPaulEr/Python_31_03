prenoms = ["Paul", "Ernest", "Martin", "p"]
noms = ["Dupont", "Lefebvre", "Aigouyi"]
nations = ["fr", "fr", "fr"]
#[(0, ('Paul', 'Dupont', 'fr')), (1, ('Ernest', 'Lefebvre', 'fr')), (2, ('Martin', 'Aigouyi', 'fr'))]

nations = nations * 10
for index, nation in enumerate(nations):
    nations[index] = nation.upper()

noms = noms * 10
for index, nom in enumerate(noms):
    noms[index] = nom.upper()

print(prenoms, noms, nations)
#['PAUL', 'ERNEST', 'MARTIN', 'p'] ['DUPONT', 'LEFEBVRE', 'AIGOUYI'] ['FR', 'FR', 'FR'] 
print("end")
