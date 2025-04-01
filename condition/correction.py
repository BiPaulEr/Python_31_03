#Exercice 1

age = input("Rentrez votre age ")
age = int(age)

if age > 17:
    print("Majeur")
else:
    print("Mineur")


#Exercice 2

score = 82

if score > 89:
    print("A")
elif score > 79:
    print("B")
elif score > 69:
    print("C")
elif score > 59:
    print("D")
elif score > 49:
    print("E")
else:
    print("F")

#Exercice 3
number = 20
print("Impair") if number%2 else print("Pair")