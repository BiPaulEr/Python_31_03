prenoms = ["paul", "ernest", "martin"]

import copy
prenoms2 = copy.deepcopy(prenoms)

prenoms.append("QUUUUUUUOI")

print(prenoms)  #['paul', 'ernest', 'martin', 'QUUUUUUUOI']
print(prenoms2) #['paul', 'ernest', 'martin']