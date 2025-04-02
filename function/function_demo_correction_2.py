liste_brute = [5, 15, None, 10, 20]

def nettoyer_donnee(liste):
    liste_tmp = []
    for element in liste:
        if element != None:
            liste_tmp.append(element)
    return liste_tmp

liste_sans_None = nettoyer_donnee(liste_brute)

def filter_donnee(liste):
    liste_tmp = []
    for element in liste:
        if element <= 10 and element >= 0:
            liste_tmp.append(element)
    return liste_tmp

liste_sans_None_Entre_0_10 = filter_donnee(liste_sans_None)

def analyser_donnee(liste):
    liste_tmp = nettoyer_donnee(liste)
    liste_tmp = filter_donnee(liste_tmp)
    return liste_tmp

print(liste_brute) #[5, 15, None, 10, 20]
print(liste_sans_None) #[5, 15, 10, 20]
print(liste_sans_None_Entre_0_10) #[5, 10]

print(analyser_donnee(liste_brute)) #[5, 10]