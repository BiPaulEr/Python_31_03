class Voiture():
    marque = "Peugeot"
    modele = "Partner"

    def __init__(self, imma, couleur = "rouge"):
        self.immatriculation = imma
        self.couleur = couleur
    
    def display(self):
        print(f"La marque est {self.marque} du modele {self.modele} avec la plque {self.immatriculation}")
        print(self.couleur)
   
voiture1 = Voiture("EK-103-TY", "jaune")

voiture2 = Voiture("IK-790-YU")

voiture3 = Voiture("ZR-700-PU")

voiture1.display()
voiture2.display()
voiture3.display()

print("end")