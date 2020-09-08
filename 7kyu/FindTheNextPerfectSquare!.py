def find_next_square(sq):
    import math
    if pow(sq, 0.5) %1 ==0:
        return int(pow(pow(sq, 0.5)+1, 2))
    return -1

def find_next_square_best(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
    
print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))