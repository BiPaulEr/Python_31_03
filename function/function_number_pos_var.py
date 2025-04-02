liste1 = ["1", "2", "3"]
liste2 = ["3", "4", "5"]
liste3 = ["6", "7", "8"]
"""
print(list(zip(liste1, liste2)))
print(list(zip(liste1, liste2, liste3)))
print(list(zip(liste1, liste2, liste3, liste1, liste2, liste3)))"""
#[('1', '3', '6', '1', '3', '6'), ('2', '4', '7', '2', '4', '7'), ('3', '5', '8', '3', '5', '8')]

def function(*args):
    print(args)

function("A", "B") #('A', 'B')
function("A", "B", "C") #('A', 'B', 'C')

def function_entrop(arg1, *args):
    print(args)

#function_entrop() #
function_entrop("A") #()
function_entrop("A", "B") #('B',)
function_entrop("A", "B", "C") #('B', 'C')

def function_nom(**kwargs):
    print(kwargs)

function_nom(a="3", b='4', c="T") #{'a': '3', 'b': '4', 'c': 'T'}
function_nom() #{}

def function_nom_en_trop(age = 18, **kwargs):
    print(kwargs)

function_nom_en_trop(a="3", b='4', c="T") #{'a': '3', 'b': '4', 'c': 'T'}
function_nom_en_trop(age= 90, b = "T3") # {"b": "T3"}
function_nom_en_trop() # {}