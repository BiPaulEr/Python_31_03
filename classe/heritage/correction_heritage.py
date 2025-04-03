class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def description(self):
        print(f"Voiture : {self.marque}, {self.modele}")
    
class VoitureSport(Voiture):
    def __init__(self, marque, modele, vitesse_max):
        self.vitesse_max = vitesse_max
        super().__init__(marque, modele)

    def description(self):
        super().description()
        print(f"Sport VM : {self.vitesse_max}")

class VoitureFamiliale(Voiture):
    def __init__(self, marque, modele, num_place):
        self.num_place = num_place
        super().__init__(marque, modele)
        
    def description(self):
        super().description()
        print(f"Num Places : {self.num_place}")

voituresport = VoitureSport("Peugeot", "GTI 205", "223")
voituresport.description()

voitureFamiliale = VoitureFamiliale("Peugeot", "Kangoo", "7")
voitureFamiliale.description()