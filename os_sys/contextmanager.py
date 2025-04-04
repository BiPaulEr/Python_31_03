class ContextManagerSimple():
    def __init__(self, variable):
        self.variable = variable
    def __enter__(self):
        print(self.variable)
        print("Preparer le contexte")
        return "Object"

    def __exit__(self, exc, exctype, traceback):
        if (exc):
            print("Exception detected")
            print(exctype)
        print("Sortie du context")
        return True
        

with ContextManagerSimple("variable passe au constructeur") as varaible:
    print(varaible)
    print("Interieur du contexte") 
    raise Exception("exception leve dans le contexte")
