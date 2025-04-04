class TailleInvalideException(Exception):
    pass

def verifier_taille(chaine :str):
    if len(chaine) <= 5:
        raise TailleInvalideException(f"len must be more than 5 here is {len(chaine)}")

def convertir_entier(chaine : str):
    try:
        number = int(chaine)
    except ValueError as e:
        print(f"{e}")
        return 0
    except TypeError as e:
        print(f"{e}")
        return -1
    else:
        return number
    finally:
        print("Convertion terminée")

if __name__ == "__main__":
    print(convertir_entier("3"))
    print(convertir_entier("3.5")) 
    print(convertir_entier("arbre"))
    print(convertir_entier(list()))
    try:
        verifier_taille("1234567890")
        verifier_taille("")
    except TailleInvalideException as t:
        print(f"{t}")