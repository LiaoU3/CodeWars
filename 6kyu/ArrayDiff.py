def array_diff(a, b):
    c = []
    if not b:
        return a
    for x in a:
        is_equal = False
        for y in b:
            if x == y:
                is_equal = True
                break
        if not is_equal:
            c.append(x)
    return c

def array_diff_best(a, b):
    return [x for x in a if x not in b]

print(array_diff_best([1,2,2], [2]))
print(array_diff_best([1,2,2], []))
print(array_diff_best([], [1,2]))