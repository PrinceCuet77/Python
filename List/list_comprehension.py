# List comprehension
# With the help of list comprehension, we can create a list in one line 

# Make a list of square from 1 to 10 
sq = [i**2 for i in range(1, 11)]
print(sq)

# Create a list of negative number from 1 to 10
neg = [-i for i in range(1, 11)]
print(neg)

# Make a list where store the first character from the other list which consists of strings
name = ['Rezoan', 'Shakil', 'Prince']
new_list = [ch[0] for ch in name]
print(new_list)

# Make a list where store the reverse string from other list which consists of strings
name = ['Rezoan', 'shakil', 'Prince']
l = [ch[::-1] for ch in name]
print(l)

# List comprehensive with if statement
# Make a list where store only even numbers from 1 to 10
l = [i for i in range(1, 11) if i % 2 == 0]
print(l)

l2 = [i for i in range(1, 11) if i & 1 == 0]
print(l2)

# Make a list where store only int or float variable in the form of string from the other list which consists all data types
def make_list(l) : 
    return [str(i) for i in l if (type(i) == int or type(i) == float)]

l = [True, False, (1, 2, 3), [4, 5], {4, 5}, {3:3}, 1, 'string', 4.4]
new_l = make_list(l)
print(new_l)

# List comprehensive with if else statement
# Make a list where store odd numbers as negative and even numbers as square of even numbers
l = [i**2 if (i & 1 == 0) else -i for i in range(1, 11)]
print(l)

l2 = [i**2 if (i % 2 == 0) else -1 for i in range(1, 11)]
print(l2)

# Nested list
# Using list comprehension
mat = [[i for i in range(1, 4)] for i in range(3)]
print(mat)