# Dictionary comprehension
# Make a dictionary where store square of the number from 1 to 10
dic = {i : i**2 for i in range(1, 11)}
print(dic)

# Count how many times present a specific character in the string
name = 'Rezoan Shakil Prince'
word_count = {char : name.count(char) for char in name}
print(word_count)

# Dictionary comprehension using if statement
# Make a dictionary where store only even numbers as key and square of even numbers as values
dic = {i : i**2 for i in range(1, 11) if i % 2 == 0}
print(dic)

# Dictionary comprehension using if else statement
# Make a dictionary where write 'even' when it's even otherwise write 'odd'
odd_even = {i : ('even' if (i % 2 == 0) else 'odd') for i in range(1, 11)}
print(odd_even)