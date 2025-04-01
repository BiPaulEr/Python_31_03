liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for index in range(0, len(liste), 1):
    liste[index] = liste[index] * 2
    print(index)

print(liste) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]