# Without enumerate function 
names = ['Rezoan', 'Shakil', 'Prince']

pos = 0 
for name in names : 
    print(f'{pos} : {name}')
    pos += 1
print()

# With enumerate function 
for pos, name in enumerate(names) : 
    print(f'{pos} : {name}')
print()

# Example : 01
# A list contain strings so finding desired string's index if found then return position but not found then print 'Not found'

def find(name, desired_string) : 
    for pos, value in enumerate(name) : 
        if desired_string == value : 
            return pos
    return -1

print(find(names, 'Prince'))
print()