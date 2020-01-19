name = "Harshit Vashisth"

# Using while loop
temp = ""
len = len(name) 
i = 0 
while i < len : 
    if name[i] not in temp : 
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
print()

# Using for loop
temp = ""
for i in name : 
    if i not in temp : 
        temp += i
        print(f"{i} : {name.count(i)}")