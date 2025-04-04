def decorator(function):
    def wrapper(*args):
        print("Je suis avant la fonction")
        function(*args)
        print("Je suis après la fonction")
    return wrapper

@decorator
def function_double(ARG1, ARG2):
    print(f"Je suis dans la fonction {ARG1} {ARG2}")

@decorator
def function_simple(ARG1):
    print(f"Je suis dans la fonction {ARG1}")

function_simple("VALEUR ARG1")
function_double("VALEUR ARG1", "ARG2")
