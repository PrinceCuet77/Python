example = ('one', 'two', 'three', 'one')

# Support below functions
print(example.count('one'))
print(example.index('one'))
print(len(example))
print(example[:2])

# Function returning tuple
def func(int1, int2) : 
    add = int1 + int2
    mul = int1 * int2 
    return add, mul 

print(func(2, 3))                               # Returning tuple
add, mul = func(4, 5)                           # Unpacking tuple two variable
print(add)
print(mul)

# Looping into tuple
mixed = (1, 2.0, 'three')

for i in mixed :                                    # Using for loop
    print(i, end = ' ')
print()

i = 0
while i < len(mixed) :                              # Using while loop
    print(mixed[i])
    i += 1

# Tuple with one element
one = (1)
word = ('word')
print(type(one))
print(type(word))

one1 = (1,)
word1 = ('word',)
print(type(one1))
print(type(word1))

# Tuple without paranthesis
num = 'one', 'two', 'three'
num1 = 1, 2, 3

print(type(num))
print(type(num1))

# Tuple unpacking 
st = ('prince', 23)
name, age = st                                      # Unpacking 
print(name)
print(age)

# List inside tuple 
value = (1, 2, ['three', 'four'])
value[2].pop()
value[2].append('five')
print(value)

# range(), tuple(), max(), min(), sum() functions
t = tuple(range(1, 6))
print(max(t))
print(min(t))
print(sum(t)) 