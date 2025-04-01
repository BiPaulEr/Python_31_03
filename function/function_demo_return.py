def function_name(name):
    name = name + " paul ernest"
    return name.upper()

name = "martin"

result = function_name(name) 

print(result) #MARTIN PAUL ERNEST

def function_name_return_none(name):
    name = name + " paul ernest"

result = function_name_return_none(name) 

print(result) #None

def return_name_family():
    return "Paul", "Ernest", "Martin"

prenom1, prenom2, prenom3 = return_name_family() 

print(result) # ('Paul', 'Ernest', 'Martin')