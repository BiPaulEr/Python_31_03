import time

def cache(function):
    dictionnaire = {}
    def wrapper(*args):
        if args in dictionnaire:
            print("cached")
            return dictionnaire[args]
        result = function(*args)
        dictionnaire[args] = result
        return result
    return wrapper

@cache
def couteuse(a, b):
    result = a + b
    time.sleep(2)
    return result

now = time.time_ns()

couteuse(3, 5)
couteuse(-2, 5)
couteuse(-3, 5)
couteuse(3, 5)
couteuse(-3, 5)
couteuse(-2, 5)

delta = (time.time_ns() - now)*(10**-9)
print(f"L'algorithme a pris {delta} secondes")