from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def jouer(self):
        pass
    
    @abstractmethod
    def accorder(self):
        pass

class Guitare(Instrument):
    def jouer(self):
        print("Dring")
    def accorder(self):
        pass

class Piano(Instrument):
    def jouer(self):
        print("Piaout")
    def accorder(self):
        pass
    
class Batterie(Instrument):
    def jouer(self):
        print("Boom")
    def accorder(self):
        pass

def faire_jouer(liste_instrument : list[Instrument]) -> None :
    for instrument in liste_instrument:
        instrument.jouer()

liste_instrument = [Guitare(), Piano(), Batterie()]
faire_jouer(liste_instrument)
