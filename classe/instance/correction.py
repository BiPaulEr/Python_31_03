class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def saluer(self):
        print(f"Salut, je suis {self.prenom} {self.nom}")
    
personne1 = Personne("Alice", "Merveille")
personne1.saluer()

personne2 = Personne("Pierre", "Jean")
personne2.saluer()
print("end")