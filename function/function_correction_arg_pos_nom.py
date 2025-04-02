def afficher_prix_total(prix_entree, prix_plat_principale, *args, prix_desert = 10, **kwargs):
    somme = sum((prix_entree, prix_plat_principale, prix_desert)) + sum(args)
    print(f"Le prix de repas est {somme}")
    print(kwargs)

afficher_prix_total(10, 5, 5)
afficher_prix_total(10, 5)

prix_commande = (5, 7, 9)
afficher_prix_total(10, 20, *prix_commande)

details_command_arg = {"client":'John Doe', "table":5,"alergie":'sans gluten'}
afficher_prix_total(10, 20, **details_command_arg)