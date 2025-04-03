class Secret:
    def __init__(self):
        self.__nom = "Not so secret"
        self.__private_method() 

    def __private_method(self):
        print("Private method called")

    def reveal_secret(self):
        print(self.__nom)  



obj = Secret()
#print(obj.__nom)
#obj.__private_method()
obj.reveal_secret()
print(obj._Secret__nom)
obj._Secret__private_method()
print("ned")

"""
print(obj.__private_method())  # Provoque une erreur, AttributeError
print(obj._Secret__secret)  # Accessible via le name mangling
print(obj._Secret__private_method())  # Accessible via le name mangling"
"""