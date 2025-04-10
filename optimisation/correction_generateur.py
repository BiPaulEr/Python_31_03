#Exercice1

maximum = 11
def pair(max):
    for i in range(1, max+1, 2):
        yield i
pair_gen = (i for i in range(1, maximum+1, 2))

for i1, i2 in zip(pair(maximum), pair_gen):
    print(i1, i2)

#Exercice2
print("\n\nCarre\n")
def carre(max):
    for i in range(1, max+1, 1):
        yield i**2

carre_gen = (i**2 for i in range(1, maximum+1))
for i1, i2 in zip(carre(maximum), carre_gen):
    print(i1, i2)

#Exercice 3
print("\n\fibo\n")
def fibonnaci(max):
    a, b = 0, 1
    for _ in range(0, max):
        yield a
        a, b = b, a+b

fib = fibonnaci(maximum)
for i in fib:
    print(i)