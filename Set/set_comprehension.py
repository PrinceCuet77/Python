# Set comprehension
# Make a set where store square of the numbers from 1 to 10
st = {i**2 for i in range(1, 11)}
print(st)

# Make a set where store the first character of the list which consists of strings
name = ['Rezoan', 'Shakil', 'Prince']
name_st = {char[0] for char in name}
print(name_st)

# Set comprehension using if statement
# Make a set where store even negative numbers from 1 to 10 
st = {-i for i in range(1, 11) if i % 2 == 0}
print(st)

# Set comprehensive using if else statement 
# Make a set where store even positive numbers and odd negative numbers from 1 to 10
st2 = {i if (i % 2 == 0) else -i for i in range(1, 11)}
print(st2)