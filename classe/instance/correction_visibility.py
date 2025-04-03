class Banque:
    def __init__(self, compte):
        self.__compte = compte

    def __operation(self, montant):
        self.__compte += montant
    
    def depot(self, montant):
        if (montant > 0):
            self.__operation(montant)
    
    def retrait(self, montant):
        if (montant > 0):
            self.__operation(-1 * montant)

    def display(self):
        print(f"Le solde du compte est de {self.__compte}")
        
banque = Banque(1000)
banque.display()
banque.depot(500)
banque.display()
banque.retrait(500)
banque.display()

#banque.__compte += 100000000000000
#banque._Banque__compte += 10000000000000000
#banque.display()

#banque.__operation()
#banque._Banque__operation(100)


