# https://www.codewars.com/kata/55df87b23ed27f40b90001e5/train/python

# def calc_special( lastDigit,base ):
#     n = 0 
#     while True:
#         for k in range (2,base):
#             num  = (lastDigit*(base**(n+1) -1 ))/(base*k -1)
#             if num % 1 == 0:
#                 if base == 10:
#                     return str(int(num))
#                 elif base == 16:
#                     return hex(int(num))[2:]
#                 elif base == 8:
#                     return oct(int(num))[2:]
#         n += 1
def calc_special(d, b):
    rep = {10:'d', 8:'o', 16:'x'}[b]
    n = format(d, rep)
    while True:
        prod = format(d * int(n, b), rep)
        if n[-1:]+n[:-1] == prod: return n
        n = prod[-len(n):]+n[-1:]
print( calc_special(2, 10))