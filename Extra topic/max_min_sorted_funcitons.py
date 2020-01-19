# Advanced max(), min(), sorted() function
def find_len(item) : 
    return len(item)

name = ['Rezoan', 'Shakil', 'CUET']
print(max(name, key = find_len))                                            # Finding name which one is highest length
print(min(name, key = find_len))                                            # Finding name which one is lowest length
print()

student = {
    'Rezoan' : {'score' : 90, 'age' : 22}, 
    'Shakil77' : {'score' : 70, 'age' : 19},
    'Prince' : {'score' : 76, 'age' : 23}
}

# Returning string like 'Rezoan'
print('Max function : ')
print(max(student, key = find_len))
print(max(student, key = lambda item : student[item]['age']))
print()

print('Min function : ')
print(min(student, key = find_len))
print(min(student, key = lambda item : student[item]['age']))
print()

student2 = [
    {'name' : 'Rezoan', 'score' : 90, 'age' : 22}, 
    {'name' : 'Shakil77', 'score' : 70, 'age' : 19}, 
    {'name' : 'Prince', 'score' : 76, 'age' : 23}
]

# Returning dictionary like {'name' : 'Rezoan'}
print('Max function : ')
print(max(student2, key = find_len))
print(max(student2, key = lambda item : len(item.get('name'))))                 # Finding longest length's string
print(max(student2, key = lambda item : item.get('score')))                     # Finding highest score
print(max(student2, key = lambda item : item.get('age')).get('score'))          # Showing the score
print()

print('Min function : ')
print(min(student2, key = find_len))
print(min(student2, key = lambda item : item.get('score')))
print(min(student2, key = lambda item : item.get('age')))
print()

# Returning list like : [{'name' : 'Rezoan'}, {'name' : 'Shakil'}]
print('Sorted function : ') 
print(sorted(student2, key = lambda item : item.get('score')))                  # Sorted by score
print(sorted(student2, key = lambda item : item.get('age')))                    # Sorted by age
print(sorted(student2, key = lambda item : item.get('age'), reverse = True))    # Reversing the above one