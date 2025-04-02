def generateur():
    print("Debut generateur")
    for i in ["A", "B", "C"]:
        yield i 
        print("Rzprise")
    print("Fin generateur")

gen = generateur()

for i in generateur():
    print(i)

for i in generateur():
    print(i)

"""
print(next(gen))

print(next(gen))

print(next(gen))

print(next(gen))
"""