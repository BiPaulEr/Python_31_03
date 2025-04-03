def generateur():
    print("Debut generateur")
    i = 0
    while True:
        yield i 
        i += 1
        print("Reprise")

gen = generateur()
list(gen)