import argparse

def saluer(nom, age):
    print(f"Bonjour {nom} {age}")

parser = argparse.ArgumentParser(description="Dire bonjour à moi")
parser.add_argument('nom', type=str, help='le nom de famille')
parser.add_argument('--age', default=18, type=str, help='le nom de famille')
parser.add_argument('--object', type=str, help='le nom de famille')

args = parser.parse_args()
if args.object:
    print(args.object)
else:
    print(args.object)
saluer(args.nom, args.age)

