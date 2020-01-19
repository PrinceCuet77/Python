# Set - unordered collection of unique items 
# Removing all duplicate element in the list, tuple
l = [1, 1, 1, 2, 3, 3, 4, 5, 6, 5, 5, 6] 
l1 = list(set(l))
print(l) 
print(l1)

# Some important notes about set
# Set doesn't store list or dictionary but store tuple and any other data type like int, double, float, string, char
s = {1, 1.1, 'string', 'P', (3, 4, 5)}
print(s)

# Using loop
for i in s :                                # Unorderly print
    print(i)

# Conditional statement
if 'string' in s : 
    print("present")
else : 
    print("not present")

# Union in the set 
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s3 = s1 | s2                                # Taking all of the element of the two sets
print(s3)

# Intersection in the set
s4 = s1 & s2                                # Taking common of the two sets
print(s4)

# Some methods of set
s = {1, 4, 5, 2}

# add() method 
s.add(5)                                    # 5 exist so no add
print(s)

s.add(50)                                   # 50 exist so add to set 's'
print(s)

# remove() method
s.remove(4)                                 # Removing 4 but if not present in set then showing error 
print(s)

# discard() method 
s.discard(55)                               # Main work is deleting 55 element but not present in set so no deletion is occured
print(s)

s.discard(50)                               # Deleting 50 from set 's' 
print(s)

# copy() method 
s1 = s.copy()
print(s)
print(s1) 

# clear() method
s1.clear()
print(s1)