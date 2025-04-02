noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

#Exercice 1
etudiants = list(zip(noms, scores))
print(etudiants) #[('Alice', 85), ('Bob', 92), ('Charlie', 78)]

etudiants_sup_17_20 = list(filter(lambda x: x[1] >= 17, map(lambda x: (x[0], x[1] / 5), etudiants)))
print(etudiants_sup_17_20) #[('Alice', 17.0), ('Bob', 18.4)]


etudiants_sup_17_20_compr = [(prenom, note / 5) for prenom, note in zip(noms, scores) if note/5 >= 17]
print(etudiants_sup_17_20_compr) #[('Alice', 17.0), ('Bob', 18.4)]