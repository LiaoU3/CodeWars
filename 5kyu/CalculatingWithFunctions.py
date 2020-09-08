# This time we want to write calculations using functions and get the results.
# Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

# Requirements:
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# eight(divided_by(three()))
# Divison should be integer division. For example, this should return 2, not 2.666666...:

# def zero(a = None):
#     if a == None:
#         return '0'
#     else:
#         if a[0] =='+':
#             return int(a[1])
#         elif a[0] =='-':
#             return 0 - int(a[1])
#         else :
#             return 0
# def one(a = None):
#     if a == None:
#         return '1'
#     else:
#         if a[0] =='+':
#             return 1 + int(a[1])
#         elif a[0] =='-':
#             return 1 - int(a[1])
#         elif a[0]=='*':
#             return 1 * int(a[1])
#         else :
#             return 1 // int(a[1])
# def two(a = None):
#     if a == None:
#         return '2'
#     else:
#         if a[0] =='+':
#             return 2 + int(a[1])
#         elif a[0] =='-':
#             return 2 - int(a[1])
#         elif a[0]=='*':
#             return 2 * int(a[1])
#         else :
#             return 2 // int(a[1])
# def three(a = None):
#     if a == None:
#         return '3'
#     else:
#         if a[0] =='+':
#             return 3 + int(a[1])
#         elif a[0] =='-':
#             return 3 - int(a[1])
#         elif a[0]=='*':
#             return 3 * int(a[1])
#         else :
#             return 3 // int(a[1])
# def four(a = None):
#     if a == None:
#         return '4'
#     else:
#         if a[0] =='+':
#             return 4 + int(a[1])
#         elif a[0] =='-':
#             return 4 - int(a[1])
#         elif a[0]=='*':
#             return 4 * int(a[1])
#         else :
#             return 4 // int(a[1])
# def five(a = None):
#     if a == None:
#         return '5'
#     else:
#         if a[0] =='+':
#             return 5 + int(a[1])
#         elif a[0] =='-':
#             return 5 - int(a[1])
#         elif a[0]=='*':
#             return 5 * int(a[1])
#         else :
#             return 5 // int(a[1])
# def six(a = None):
#     if a == None:
#         return '6'
#     else:
#         if a[0] =='+':
#             return 6 + int(a[1])
#         elif a[0] =='-':
#             return 6 - int(a[1])
#         elif a[0]=='*':
#             return 6 * int(a[1])
#         else :
#             return 6 // int(a[1])
# def seven(a = None):
#     if a == None:
#         return '7'
#     else:
#         if a[0] =='+':
#             return 7 + int(a[1])
#         elif a[0] =='-':
#             return 7 - int(a[1])
#         elif a[0]=='*':
#             return 7 * int(a[1])
#         else :
#             return 7 // int(a[1])
# def eight(a = None): 
#     if a == None:
#         return '8'
#     else:
#         if a[0] =='+':
#             return 8 + int(a[1])
#         elif a[0] =='-':
#             return 8 - int(a[1])
#         elif a[0]=='*':
#             return 8 * int(a[1])
#         else :
#             return 8 // int(a[1])
# def nine(a = None): 
#     if a == None:
#         return '9'
#     else:
#         if a[0] =='+':
#             return 9 + int(a[1])
#         elif a[0] =='-':
#             return 9 - int(a[1])
#         elif a[0]=='*':
#             return 9 * int(a[1])
#         else :
#             return 9 // int(a[1])

# def plus(x): 
#     return '+' + x
# def minus(x):
#     return '-' + x
# def times(x):
#     return '*' + x
# def divided_by(x):
#     return '/' + x

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))