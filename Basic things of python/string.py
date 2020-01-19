first_name = "Rezoan" 
last_name = "Shakil"

full_name = first_name + " " + last_name; 
print(full_name)

print(full_name + " 77")                                # No error 
print(full_name + str(77))                              # No error

print(full_name * 3)                                    # Print full_name 3 times

# String formatting 
name = "prince"
age = 22
print(f"Name : {name} and Age : {age+2}")

# String indexing
lan = "python"
# p = 0, -6
# y = 1, -5
# t = 2, -4
# h = 3, -3
# o = 4, -2
# n = 5, -1

print(lan[2])                                           # Showing 't' the 2nd position character
print(lan[-2])                                          # Showing 'o' the 4th from first or 2nd from last position character

# String slicing / selecting sub sequences
# Syntax - [start argument : stop argument -1]
print(lan[2:5])
print(lan[:])                                           # Show full string
print(lan[:3])                                          # Starting in '0' position
print(lan[3:])                                          # Finish till last position
print(lan[-3:6])                                        # Starting in '-3' position 

# Step argument 
print(lan[2:5:1])                                       # Third one is 'step argument'
print(lan[2:5:2])                                       # Jump 2 character
print(lan[::-1])                                        # String reverse - trick
print(lan[-1::-1])                                      # reverse

# String method 
name = "ReZoAn sHaKiL"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.count('a'))                                  # Case sensetive
print(name.lower().count('a'))                          # Show all lower and upper

# Strip methods
name = "    Pri    nce     "
dots = "-------------" 
print(name + dots)
print(name.lstrip() + dots)                             # Remove only left spaces
print(name.rstrip() + dots)                             # Remove only right spaces
print(name.strip() + dots)                              # Remove left and right spaces 
print(name.replace(" ", "") + dots)                     # Remove all spaces in the variable

# replace() and find() methods
st = "she is beautiful and she is good dancer"
print(st.replace("is", "was"))

print(st.find("is"))                                    # Showing the position of "is"(0 indexing)
print(st.find("is", 5))                                 # Finding "is" in 5th index
print(st.find("is", 5, 10))                             # Start at 5 and stop at 10 and can't find so result -1

# center() method
name = "prince"
print(name.center(len(name)+4, "*"))

# in keyword
name = "Prince"
if 'C' in name : 
    print("'c' is present")
else : 
    print("'c' is not present") 

# String print using while loop 
i = 0
while i < len(name) : 
    print(name[i])
    i += 1
print()

for i in name : 
    print(i)

# Some string
t = (1, 2, 3)
l = [1, 2, 3]

s = str(t)
print(s)
print(type(s))
print(len(s))

s = str(l)
print(s)
print(type(s))
print(len(s))