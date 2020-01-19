# Doc string 
def add(a, b) : 
    '''Taking 2 arguments and returning sum of two numbers'''
    return a + b 

print(add(1, 2))
print(add.__doc__)                                              # Doc string calling
print(len.__doc__)
print(sum.__doc__)
print(max.__doc__)
print(min.__doc__)
print(sorted.__doc__)

print()

print(help(add))                                                # Showing function defination and details things
print(help(len))
print(help(sum))
print(help(max))
print(help(min))
print(help(sorted))