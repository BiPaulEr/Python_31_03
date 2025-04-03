class Simplest():
    attribut_de_classe = "Je suis un attribut de classe"

print(type(Simplest))
print(Simplest.attribut_de_classe) 

simple1 = Simplest()
print(simple1.attribut_de_classe) 

simple2 = Simplest()
simple2.attribut_de_classe = "JE suis definit dans l'isntance"

Simplest.attribut_de_classe = "Retro"
print(simple1.attribut_de_classe) 
print(simple2.attribut_de_classe) 



print("end")