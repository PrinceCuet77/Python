numbers = [1, 2, 3]
print(numbers)
print(numbers[2])

words = ['word1', 'word2', 'word3']
print(words)
print(words[:2])                                                # Support slicing

mixed = [1, 2.0, 'three', None]
print(mixed)
print(mixed[-1])

mixed[2] = 'two'
print(mixed)                                                    # Replacing 

mixed[2:] = 'two'                                               # Replacing rest with characters
print(mixed)                                        

mixed[2:] = ['two', 'three']                                    # Replacing rest with string
print(mixed)                                        

# Add element to list
fruits = ['mango', 'banana']
fruits.append('apple')                                          # Add element at last
fruits.append('pine-apple')

print(fruits)

fruit1 = ['mango', 'banana']
fruit1.insert(1, 'grapes')                                      # Insert at position 1(0 indexing)
print(fruit1)

fruit2 = ['apple', 'pine-apple']
fruits = fruit1 + fruit2                                        # Add two list
print(fruits)

fruit1.extend(fruit2)                                           # Add fruit2 at the last of fruit1(more efficient)
print(fruit1)

fruit1.append(fruit2)                                           # Make 2D list
print(fruit1)

# delete methods
fruit1 = ['mango', 'banana', 'grapes', 'apple', 'kiwi']
fruit1.pop()                                                    # Popped from last
fruit_popped = fruit1.pop(1)                                    # pop(index) - (0 indexing)
print(fruit1)
print(fruit_popped)

del fruit1[0]                                                   # 0 indexing
print(fruit1)

fruit1.remove('apple')                                          # Removing element if not found then show error
print(fruit1)

# in keyword with list
fruit1 = ['mango', 'banana', 'grapes', 'apple', 'kiwi']
if 'mango' in fruit1 : 
    print("mango is present")
else : 
    print("mango is not present")

# some list function
fruit1 = ['mango', 'banana', 'grapes', 'apple', 'kiwi', 'banana']
print(fruit1.count('banana'))   

fruit1_copy = fruit1.copy()
print(fruit1_copy)

fruit1_sorted = sorted(fruit1)
print(fruit1_sorted)

print(fruit1_copy)
fruit1_copy.reverse()                                                   # Last element become first element not reverse sorted
print(fruit1_copy)

fruit1_copy.clear()
print(fruit1_copy)

fruit1.sort()
print(fruit1)

# '==' vs 'is'
fruit1 = ['mango', 'kiwi', 'apple']
fruit2 = ['mango', 'kiwi', 'apple']

if fruit1 == fruit2 : 
    print("Equal")
else : 
    print("Not equal")

if fruit1 is fruit2 : 
    print("Equal")
else :
    print("Not equal")

# String to list conversion
st = "prince 22"
lt = st.split()                                 # Separator is space
print(lt)

st = "prince,22"
lt1 = st.split(',')                              # Separator is comma
print(lt1)

print(' '.join(lt))                              # Joining through space
print(','.join(lt))                              # Joining through comma

# For loop into list 
fruit = ['mango', 'apple', 'kiwi']

for i in fruit : 
    print(i)

# While loop into list
i = 0 
while i < len(fruit) : 
    print(fruit[i])
    i += 1

# List inside list 
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for subMat in mat :                                     # For looping
    for i in subMat : 
        print(i, end = ' ')
    print()

i = 0 
while i < len(mat) :                                    # While looping
    j = 0 
    while j < len(mat[i]) : 
        print(mat[i][j], end = ' ')
        j += 1
    i += 1
    print()

st = "prince"
print(type(st))
print(type(mat))

# More about list 
number = list(range(1, 6))
print(number)

num = [1, 2, 3, 4, 5, 6, 1]
print(num.index(1))                                 # num.index(value)
print(num.index(1, 3))                              # num.index(value, starting position)
# print(num.index(1, 2, 5))                         # In the range of 2 to 5 there are no 1 so produce error                     
# num.index(value, starting position, ending position)

# List in function 
def makeNeg(l) : 
    neg = [] 
    for i in l : 
        neg.append(-i)
    return neg 

print(makeNeg(number))

# min() and max() function
l1 = [100, 30, 60]
print(min(l1))
print(max(l1))

# Join two list by '+' operator
l1 = [1, 2] 
l2 = [3, 4]
l3 = l1 + l2 
print(l3)

# sum() function
l = list(range(1, 6))
print(sum(l))