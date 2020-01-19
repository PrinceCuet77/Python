# Example : 01 
def add(a, b) : 
    return a + b 

add2 = lambda a, b : a + b                  # 'function_name' = lambda 'parameters' : 'return_type'

print(add(4, 5))
print(add2(4, 5))

# Example : 02 
def multiply(a, b) : 
    return a * b 

multiply2 = lambda a, b : a * b 

print(multiply(4, 5))
print(multiply2(4, 5))

# Calling function and lambda 
print(add)
print(add2)
print(multiply)
print(multiply2)

# Example : 03
# Cheching a number is even or not 
is_even = lambda a : a % 2 == 0 

print()
print(is_even(2))
print(is_even(3))

# Example : 04 
# Printing the last character of the string 
last_char = lambda s : s[-1] 
print(last_char('Prince'))
print()

# Example : 05 
# Lambda expression with if else condition 
checking = lambda a : True if a > 5 else False 
print(checking(3))
print(checking(6))
print()