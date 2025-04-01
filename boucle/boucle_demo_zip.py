prenoms = ["Paul", "Ernest", "Martin", "P"]
noms = ["Dupont", "Lefebvre", "Aigouyi"]
nations = ["fr", "fr", "fr"]
#[('Paul', 'Dupont'), ('Ernest', 'Lefebvre'), ('Martin', 'Aigouyi')]

for prenom, nom, nation in zip(prenoms, noms, nations):
    print(prenom, nom, nation)

print(prenoms) 
print("end")
