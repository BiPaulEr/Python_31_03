import argparse

livres = [
    {"titre": "Les Misérables", "auteur": "Victor Hugo", "annee_publication": 1862},
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee_publication": 1943},
    {"titre": "Candide", "auteur": "Voltaire", "annee_publication": 1759}
]

parser = argparse.ArgumentParser("Mettre à jour la bilbiothèque de livre")
subparsers = parser.add_subparsers(dest='command', help='Commandes utilisateur')

add_parser = subparsers.add_parser('add', help='Ajouter un nouvel utilisateur')
add_parser.add_argument("titre", help="Titre du livre", type=str)
add_parser.add_argument("--auteur", default="Auteur Inconnue", help="Auteur du livre", type=str)
add_parser.add_argument("--annee", required=True, default=-99999999, help="Annee du livre", type=int)

look_parser = subparsers.add_parser('look', help='Chercher un livre un nouvel utilisateur')
look_parser.add_argument("titre", help="Titre du livre", type=str)

list_parser = subparsers.add_parser('list', help='Lister les livres')
list_parser.add_argument('--mode', default="titre", choices=['titre', 'annee_publication', 'auteur'], help="Couleur préférée")

args = parser.parse_args()

def recherche():
    liste_titre = list(map(lambda x : x["titre"], livres))
    if args.titre in liste_titre:
        index = liste_titre.index(args.titre)
        print(livres[index])
    else:
        print("Livre inconnu")

def ajouter():
    if args.titre in map(lambda x : x["titre"] ,livres):
        print("Livre already in the biblio")
        exit(0)
    livres.append({"titre": args.titre, "auteur": args.auteur, "annee_publication": args.annee})
    print(livres)

def lister():
    liste = list(map(lambda x : x[args.mode], livres))
    print(liste)

if args.command == "add":
    ajouter()
elif args.command == "look":
    recherche()
else:
    lister()
