# Generator 
# Example : 01 
# Showing the even number using generator 
def even_generator(n) : 
    for num in range(2, n+1, 2) : 
        yield(num)

even_num = even_generator(20) 
for num in even_num :               # Print for only one time because of generator
    print(num)

for num in even_num : 
    print(num)
print()

# Generator comprehension 
g = (i**2 for i in range(10))

for value in g : 
    print(value)