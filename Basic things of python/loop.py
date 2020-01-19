# For loop
for i in range(5) : 
    print(f"Print : {i}")
print()

for i in range(1, 5) :                          # range(start argument, stop argument-1)
    print(f"Print : {i}")
print()

# While loop
i = 0 
while i < 5 : 
    print(f"Print : {i}")
    i += 1
print()

# Step argument
for i in range(0, 5, 1) :                       # range(start argument, stop argument-1, step argument)
    print(i)
print()

for i in range(0, 5, 2) :                       # Step argument : 2
    print(i)                                    # Print 0, 2, 4
print()

for i in range(4, -1, -1) :                     # Reverse print
    print(i)
print()

for i in range(4, -1, -2) :                     # Step argument : -2 for reverse print
    print(i)
print()