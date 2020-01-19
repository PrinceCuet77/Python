value = "12345"

# Using while loop
len = len(value) 
i = total = 0 
while i < len : 
    total += int(value[i])
    i += 1 

print(total)

# Using for loop
total = 0 
for i in value : 
    total += int(i)

print(total)