def decorateur_with_arguments(number_rep):
    def decorator(function):
        def wrapper(*args):
            for i in range (0, number_rep):
                function(*args)
        return wrapper
    return decorator

@decorateur_with_arguments(10)
def function_double(ARG1, ARG2):
    print(f"Je suis dans la fonction {ARG1} {ARG2}")

@decorateur_with_arguments(5)
def function_simple(ARG1):
    print(f"Je suis dans la fonction {ARG1}")

function_simple("VALEUR ARG1")
function_double("VALEUR ARG1", "ARG2")
