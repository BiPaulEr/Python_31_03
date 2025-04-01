#Exercice 1

compteur = 10
while compteur > -1:
    print(compteur)
    compteur = compteur -1

#Exercice 2
nombres = [15, 99, 25, 50]
index = 0
while index < len(nombres) and nombres[index] < 50:
    index = index + 1

if index < len(nombres):
    print("result", nombres[index])

#Exercice 3
mdp = input(" mot de passe ? ")
while mdp != "Python2024":
    mdp = input(" ERREUR : mot de passe ? ")
print("BRAVO")