print(min(1, 2, 3))
print(min(-3, 9, 10, 23))
print(min(-3, 9, 10, 23,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3))

def minimum(arg1, *args):
    if not args:
        return arg1
    min_element = arg1
    for element in args:
        if element < min_element:
            min_element = element
    return min_element
    
print(minimum(1))
print(minimum(1, 2, 3))
print(minimum(-3, 9, 10, 23))
print(minimum(-3, 9, 10, 23,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3))