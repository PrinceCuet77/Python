# Creating dictionary
user = {'name' : 'prince', 'age' : 22}
print(user)
print(user['name'])
print(type(user))
print()

user1 = dict(name = 'prince', age = 22)
print(user1)
print(user1['age'])
print(type(user1))
print()

user_info = {
    'name' : 'prince', 
    'age' : 22, 
    'fav_movies' : ['coco', 'end game'], 
    'fav_food' : ['rice', 'meat'] 
}
print(user_info)
print(type(user_info))
print(user_info['fav_movies'])
print()

# Deals with keys of the dictionary 
# Checking key
if 'name' in user_info : 
    print("Present")
else : 
    print("Not present")
print()

# Checking value
if ['coco', 'endgame'] in user_info.values() : 
    print("Present")
else : 
    print("Not present")
print()

# Deals with keys of the dictionary
# Looping 
# According to keys
for key in user_info :                                    # Print only the keys 
    print(key)
print()

user_info_key = user_info.keys() 
print(user_info_key)
print(type(user_info_key))                                # Type : dict_keys 
print()

# According to keys
for user_key in user_info.keys() : 
    print(user_key)
print()

# Deals with values of the dictionary
for value in user_info.values() : 
    print(value) 
print()

user_info_value = user_info.values()
print(user_info_value)
print(type(user_info_value))                              # Type : dict_values
print()

# Deals with keys and values of the dictionary
user_info_all = user_info.items()                         # Type : dict_items 
print(user_info_all)
print(type(user_info_all))  
print()

# items() method
for key, value in user_info.items() :                     # Line tuple unpacking
    print(f"{key} : {value}")
print()

# Without key and value 
for i in user_info : 
    print(f"{i} : {user_info[i]}")
print()

# Adding items in dictionary 
user_info['fav_songs'] = ['senorita', 'cross me', 'beautiful people'] 
print(user_info)
print()

# Deleting items at last element in dictionary
user_info_popped = user_info.pop('fav_movies')                                  # pop(key) 
print(user_info_popped)                                                         # Store values
print(type(user_info_popped))
print(user_info)
print()

user_info_poppedItem = user_info.popitem()                                      # popitem()
print(user_info_poppedItem) 
print(type(user_info_poppedItem)) 
print(user_info)
print()

print()
user_info_poppedItem = user_info.popitem() 
print(user_info_poppedItem) 
print(user_info)
print()

# update() method
more_info = {
    'name' : 'Rezoan Shakil Prince',
    'fav_songs' : ['cross me', 'senorita'], 
    'fav_things' : ['bluetooth headphone', 'glass', 'pen']
}

user_info.update(more_info)                                     # If common then update or not common then add
print(user_info)
print()

user_info.update({})                                            # Nothing to update 
print(user_info)
print()

# Some dictionary methods
# dict.fromkeys() method
d = dict.fromkeys(['name', 'age'], 'unknown')                   # Making a dictionary usign first parameter list
print(d)                                                        # d = {'name' : 'unknown', 'age' : 'unknown'} 
print()

d1 = dict.fromkeys(('name', 'age'), 'unknown')                  # Using first parameter tuple
print(d1)
print()

d2 = dict.fromkeys("abc", 'unknown')                            # Using first parameter string where keys will be string characters
print(d2)                                                       # d2 = {'a' : 'unknown', 'b' : 'unknown', 'c' : 'unknown'}
print()

d3 = dict.fromkeys(range(1, 6), 'unknown')                      # Using first parameter range function 
print(d3)
print()

d4 = dict.fromkeys(['name', 'age'], ['unknown1', 'unknown2'])   # Using second parameter list
print(d4)
print()

# get() method
print(d.get('name'))                                        
print(d.get('names'))                                           # If not found then show 'None'
print()

if 'name' in d : 
    print('present')
else : 
    print('not present')
print()

if d.get('names') : 
    print('present')
else : 
    print('not present')
print()

# copy() method 
d5 = d.copy() 
print(d)
print(d5) 
print()

print(d5 == d)                                                  # Returning true when value are same
print(d5 is d)                                                  # Returning false when two dictionary are not same in memory
print()

# clear() method
print(d) 
d.clear() 
print(d)