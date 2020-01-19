# Example : 01 
# Finding even number from another list using filter function

l = [i for i in range(1, 11)]

def is_even(a) : 
    return a % 2 == 0

evenList = list(filter(is_even, l))
print(evenList)
print()

# Finding even number from another list using lambda expression
evenList2 = list(filter(lambda a : a % 2 == 0, l))
print(evenList2)