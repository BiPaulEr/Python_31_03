#Exercice 2 

mots_de_passe = ["12345678", "password123", "abc123", "pythoniscool"]

for mdp in mots_de_passe:
    if len(mdp) < 8:
        print("Mot de passe faible trouve", mdp)
        break

#Exercice 3
elements = ['pomme', 'banane', 'cerise', 'date', 'banane', 'baie']
elements_deja_affiche = []
for element in elements:
    if element in elements_deja_affiche:
        print("DEJA AFFICHE", element)
        break
    else:    
        print(element)
        elements_deja_affiche.append(element)