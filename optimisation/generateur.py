def generateur():
    print("Debut generateur")
    for i in ["A", "B", "C"]:
        yield i 
        print("Rzprise")
    print("Fin generateur")

gen = generateur()
print(gen) #<generator object generateur at 0x000001DC98D99A40>
print(type(gen)) #<class 'generator'>
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