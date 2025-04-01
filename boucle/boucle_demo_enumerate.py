prenoms = ["Paul", "Ernest", "Martin"]
#[(0, 'Paul'), (1, 'Ernest'), (2, 'Martin')]

for index, prenom in enumerate(prenoms):
    prenoms[index] = prenom.upper()

print(prenoms) #['PAUL', 'ERNEST', 'MARTIN']
print("end")
