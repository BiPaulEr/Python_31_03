import random

def f1(liste):
    if random.randint(0, 100) > 80:
        return None, f1.__name__
    else:
        liste.append(1)
        return liste
    
def f2(liste):
    if random.randint(0, 100) > 80:
        return None, f2.__name__
    else:
        liste.append(2)
        return liste

def f3(liste):
    if random.randint(0, 100) > 80:
        return None, f3.__name__
    else:
        liste.append(3)
        return liste

def f4(liste):
    if random.randint(0, 100) > 80:
        return None
    else:
        liste.append(4)
        return liste

def f5(liste):
    if random.randint(0, 100) > 80:
        return None
    else:
        liste.append(5)
        return liste

liste = list()
liste = f1(liste)
if liste[0]:
    liste = f2(liste)
    if liste[0]:
        liste = f3(liste)
        if liste:
            liste = f4(liste)
            if liste:
                liste = f5(liste)
print(liste)


