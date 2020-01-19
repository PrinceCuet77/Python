# Example : 01
# Making squares of all the elements from a list using map function

def square(a) : 
    return a ** 2

l = [i for i in range(1, 6)]
squareList = list(map(square, l))
print(squareList)
print()

# Same thing which is described above using lambda expression
squareList2 = list(map(lambda a : a ** 2, l))
print(squareList2)
print()

# Same thing which is described above using list comprehension 
squareList3 = [i ** 2 for i in l]
print(squareList3)
print()

# Example : 02 
# Finding length of all the strings from a list which contains string using map function

names = ['Rezoan', 'Shakil', 'Prince']
nameList = list(map(len, names))
print(nameList)