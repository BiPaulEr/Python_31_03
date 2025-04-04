def verificator_args(liste_arg):
    def verificator(function):
        def wrapper(*args):
            for arg, type_ in zip(args, liste_arg):
                if not isinstance(arg, type_):
                    print(f"{arg} is not {type_}")
                    return 'ERROR'
            return function(*args)
        return wrapper
    return verificator

@verificator_args([int, str])
def function_simple(number_age, string): #int
    print(f"Je suis dans la fonction {number_age} {string}")

function_simple("VALEUR ARG1", 8)
function_simple(8, "str")
function_simple(8, 8.9)
