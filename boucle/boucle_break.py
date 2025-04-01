liste = [1, "Choux", "Carotte", "Torchons", "Serviettes"]

element_a_trouve = "Carotte"

for element in liste:
    if element == element_a_trouve:
        print("TROUVE")
        break
    
print("END")