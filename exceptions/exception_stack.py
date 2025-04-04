import random

def f4(liste):
    if random.randint(0, 100) > 0:
        exce = Exception(f4.__name__)
        raise exce
    else:
        liste.append(4)
        return liste
    
def f3(liste):
    if random.randint(0, 100) > 80:
        raise Exception(f3.__name__)
    else:
        liste.append(3)
        try: 
            liste = f4(liste)
        except Exception as e:
            print(f"{e}")
            raise e
        return liste

def f2(liste):
    if random.randint(0, 100) > 80:
        raise Exception(f2.__name__)
    else:
        liste.append(2)
        try: 
            liste = f3(liste)
        except Exception as e:
            print(f"{e}")
            raise e
        return liste

def f1(liste):
    if random.randint(0, 100) > 80:
        raise Exception(f1.__name__)
    else:
        liste.append(1)
        try: 
            liste = f2(liste)
        except Exception as e:
            print(f"{e}")
            raise e
        return liste


liste = list()
try: 
    liste = f1(liste)
except Exception as e:
    print(f"{e}")

print(liste)


