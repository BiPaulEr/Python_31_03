import random

def f1(liste):
    if random.randint(0, 100) > 80:
        raise Exception(f1.__name__)
    else:
        liste.append(1)
        return liste
    
def f2(liste):
    if random.randint(0, 100) > 80:
        raise Exception(f2.__name__)
    else:
        liste.append(2)
        return liste

def f3(liste):
    if random.randint(0, 100) > 80:
        raise Exception(f3.__name__)
    else:
        liste.append(3)
        return liste

def f4(liste):
    if random.randint(0, 100) > 80:
        raise Exception(f4.__name__)
    else:
        liste.append(4)
        return liste

def f5(liste):
    if random.randint(0, 100) > 80:
        raise Exception(f5.__name__)
    else:
        liste.append(5)
        return liste

liste = list()
try: 
    liste = f1(liste)
    liste = f2(liste)
    liste = f3(liste)
    liste = f4(liste)
    liste = f5(liste)
except Exception as e:
    print(f"{e}")
else:
    print(liste)
finally:
    print("Peut inporte qu'il est une exception ou non je suis executé")




