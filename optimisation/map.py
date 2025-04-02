prenoms = ["paul", "ernest", "martin"]

print(list(map(lambda x : x.upper(), prenoms)))
print(list(map(lambda x : x.capitalize(), prenoms))) 
print(list(map(lambda x : x.lower(), prenoms)))
print(list(map(lambda x : (x.lower(),x.capitalize(),x.upper()), prenoms)))