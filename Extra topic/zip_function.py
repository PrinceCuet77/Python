# Zip function
user = ['user1', 'user2']
first_name = ['Rezoan', 'Shakil', 'Prince']
last_name = ['Hossain', 'Hossain', 'Hossain']

print(zip(user, first_name, last_name))                     # Zipping according to short one
print(list(zip(user, first_name, last_name)))
print(tuple(zip(user, first_name, last_name)))
print(set(zip(user, first_name, last_name)))
print(dict(zip(user, first_name)))
print()

# List to dictionary conversion 
example = [('a', 1), ('b', 2)]
print(dict(example))
print()

# * operator with zip function 
l = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(list(zip(*l)))
l1, l2 = zip(*l)
print(l1)
print(l2)
print()

# Example : l1 = [1, 3, 5, 7] & l2 = [2, 4, 6, 8] then output : [2, 4, 6, 8]
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]

new_list = []
for pair in zip(l1, l2) : 
    new_list.append(max(pair))
print(new_list)
print()

# Example : 02 
# Define a function which take number of list contains numbers like [1, 2, 3], [4, 5, 6], [7, 8, 9]
# And return average like : [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3] so [4.0, 5.0, 6.0]

def average_finder(*args) : 
    avg = []
    for pair in zip(*args) : 
        avg.append(sum(pair) / len(pair))       # returning float.If I want to return int so just replaced '/' by '//'
    return avg

average_finder2 = lambda *args : [sum(pair) / len(pair) for pair in zip(*args)]

print(average_finder([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(average_finder2([1, 2, 3], [4, 5, 6], [7, 8, 9]))