noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

#Exercice 1
etudiants = list(zip(noms, scores))
print(etudiants) #[('Alice', 85), ('Bob', 92), ('Charlie', 78)]

#Exercice 2
etudiants_20 = list(map(lambda x: (x[0], x[1] / 5), etudiants))
print(etudiants_20) #[('Alice', 17.0), ('Bob', 18.4), ('Charlie', 15.6)]

#Exercice 3
etudiants_sup_17 = list(filter(lambda x: x[1] >= 17, etudiants_20))
print(etudiants_sup_17) #[('Alice', 17.0), ('Bob', 18.4)]

#Exercice 4
liste_note = list(map(lambda x: x[1], etudiants_sup_17))
print(liste_note) #[17.0, 18.4]
print(sum(liste_note) / len(liste_note)) #17.7