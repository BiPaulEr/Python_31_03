prenoms = ["paul", "ernest", "martin"]


print(list(filter(lambda x : True, prenoms))) #['paul', 'ernest', 'martin']
print(list(filter(lambda x : False, prenoms))) #[]

print(list(filter(lambda x : "e" in x, prenoms))) #['ernest']