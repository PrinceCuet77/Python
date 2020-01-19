def sum(*args) :                               
    print(args)
    print(type(args))                       # args is a tuple
    total = 0
    for i in args : 
        total += i 
    print(total)

sum(1, 2, 3, 4, 5)

# *args with normal number or variable
def sum(num1, num2, *args) : 
    print(num1)
    print(num2)
    print(args)
    total = 0 
    for i in args : 
        total += i 
    print(total)

sum(1, 2, 3, 4, 5)

# Anything can be used in *args like list, tuple, set.
def sum(*args) : 
    print(args)
    total = 0 
    for i in args : 
        total += i 
    print(total)

num = [1, 2, 3, 4, 5]
num1 = (1, 2, 3, 4, 5)
num2 = {1, 2, 3, 4, 5}
sum(*num)                                   # Unpacking
sum(*num1)                                  # Unpacking
sum(*num2)                                  # Unpacking

# Example
# Taking two arguments, first of them is 'int' number and other list, tuple or set and return the power of the list, tuple or set
def solve(p, *args) : 
    if args : 
        return [i**p for i in args]
    else : 
        return "You didn't pass args" 

n = (1, 2, 3)
print(solve(3, *n))
print(solve(3))