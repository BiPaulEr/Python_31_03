#Exerice 1
for i in range(20, 26):
    print(i**2)

#Exerice 2
print("Exerice2")

somme = 0
for i in range(0, 51):
    if i%2 :
        somme = somme + i
print(somme)

somme = 0
for i in range(1, 51, 2):
    somme = somme + i
print(somme)

print(sum(range(1, 51, 2)))

#Exerice 3 
chaine = "Bonjour Python"
for carac in reversed(chaine):
    print(carac)

for index in range(-1, -len(chaine)-1, -1):
    print(chaine[index])

for index in range(len(chaine)-1, -1, -1):
    print(chaine[index])

for index in range(0, len(chaine), 1):
    print(chaine[len(chaine) -1 - index])

#Exerice 5
liste = list(range(10, -1, -1))
print(liste) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for index, valeur in enumerate(liste):
    print(index, "->", valeur)