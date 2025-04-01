def function_name(name):
    name = "DUPONT"
    print("JE suis dans la fonction")
    print("JE suis encore dans la fonction")
    print("Bonjour", name)

print(function_name) #<function function_name at 0x00000271F033A340>

name = "MARTIN"
function_name(name) 

def function_list(liste):
    liste.append("Lefebvre")

liste = ["MArtin", "Dupont"]
function_list(liste)
print(liste)
print("end")