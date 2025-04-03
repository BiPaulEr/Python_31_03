prenoms = ["paul", "ernest", "martin"]

generator = (prenom * 2 for prenom in prenoms if len(prenom) > 4)
print(generator) #<generator object <genexpr> at 0x00000201BE5D9A40>
print(type(generator)) #<class 'generator'>

liste = [prenom * 2 for prenom in prenoms if len(prenom) > 4]

prenoms.append("Poulet")

for i in liste:
    print(i) 
#ernesternest
#martinmartin

print("\nGen")
for i in generator:
    print(i)
#ernesternest
#martinmartin
#PouletPoulet

for i in generator:
    print(i)