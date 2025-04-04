import os

fichier_path = os.path.join(os.path.dirname(__file__), "fichier.txt")

with open(fichier_path, "r") as fichier:
    for line in fichier.readlines():
        print(line.rstrip())
