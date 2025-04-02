def calculer_prix_ttc(prix_ht, tva):
    prix_ttc  = prix_ht * (1 + (tva / 100))
    return prix_ttc

result1 = calculer_prix_ttc(100, 20)
print("result1", result1)

result2 = calculer_prix_ttc(100, 40)
print("result2", result2)