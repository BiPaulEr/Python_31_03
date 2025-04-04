import os

fichier_path = os.path.join(os.path.dirname(__file__), "fichier.txt")
try:
    fichier = open(fichier_path, "r")
    for line in fichier.readlines():
        print(line.rstrip())
except Exception as e:
    print(f"{e}")
finally:
    fichier.close()