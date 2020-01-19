name = input("Enter your name : ")              # Taking input as string by default    
print("Welcome " + name) 

age = input("Enter your age : ")                # 'age' is string
print(age)

print("Name : " + name + " and Age : " + age)

number_one = input("Enter first number : ")
number_two = input("Enter second number : ")
print("Total : " + number_one + number_two)     # number_one & number_two are string type

n1 = int(number_one)                            # String to int conversion
n2 = int(number_two)
value = n1 + n2
print(value);                                   # Showing int result

f1 = float(number_one)                          # String to float conversion
f2 = float(number_two)
value = f1 + f2
print(value)                                    # Showing float result

value = n1 + f2                     
print(value)                                    # Int + float = float

# Taking two value input 
name, age = input("Enter your name and age : ").split()
print(name)
print(age)

# Taking two value input seperated by comma
name, age = input("Enter your name and age separated by comma : ").split(",")
print(name)
# print(age)
print(int(age))