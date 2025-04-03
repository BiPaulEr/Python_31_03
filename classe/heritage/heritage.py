class Animal:
    def __init__(self, nom):
        self.nom = nom
    def parler(self):
        return f"Je suis un animal {self.nom}"

class Chien(Animal):
    def __init__(self, race, nom):
        self.race = race
        super().__init__(nom)

    def parler(self):
        msg = super().parler()
        return f"{self.race} {msg}"


animal = Animal("Oiseau")
chien = Chien("Labrador", "Rex")

print(animal.nom, "dit :", animal.parler())

print(chien.parler())