class Base:
    def __init__(self, valeur_Base):
        self.valeur_Base = valeur_Base
        print(f"Base init {self.valeur_Base}")

class A(Base):
    def __init__(self, valeur_A, *args):
        super().__init__(*args)
        self.valeur_A = valeur_A
        print(f"A init {self.valeur_A}")

class B(Base):
    def __init__(self, valeur_B, *args):
        self.valeur_B = valeur_B
        super().__init__(*args)
        print(f"B init {self.valeur_B}")

class C(A, B):
    def __init__(self, valeur_A, valeur_B, valeur_Base):
        super().__init__(valeur_A, valeur_B, valeur_Base)
        print("C init")

c = C("VALEUR A", "VALEUR B", "VALEUR BASE")
