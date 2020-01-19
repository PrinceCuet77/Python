# Printing the last element of the string
def last_char(st) : 
    return st[-1]

print(last_char("Prince"))

# Checking odd or even 
def oddEven(n) : 
    return n % 2

if oddEven(2) == False : 
    print("Even")
else : 
    print("Odd")

if oddEven(3) == True : 
    print("Odd") 
else : 
    print("Even")

# Checking even or not 
def isEven(n) : 
    return n % 2 == 0 

if isEven(2) == True : 
    print("Even") 
else : 
    print("Not even")

if isEven(3) == False : 
    print("Not even")
else : 
    print("Even")

# Finding greater number between two numbers
def great(n1, n2) : 
    return n1 > n2 

n1 = int(input("Frist : "))
n2 = int(input("Second : "))
if great(n1, n2) == True : 
    print(f"n1 = {n1} is greater")
else : 
    print(f"n2 = {n2} is greater")

# Finding greater number among three numbers
def gre(n1, n2, n3) : 
    return max(max(n1, n2), n3)                                     # Function inside function

print(gre(100, 40, 60))

# Checking palindrome or not
def isPalindrome(st) : 
    return st == st[::-1] 

if isPalindrome("madam") : 
    print("Palindrome")
else : 
    print("Not palindrome")

if isPalindrome("house") : 
    print("Palindrome")
else : 
    print("Not palindrome")

# Printing fibonacci
def fib(n) : 
    a = 0
    b = 1 
    if n == 1 : print(b) 
    elif n == 2 : print(a, b) 
    else : 
        print(a, b, end = " ")
        for i in range(n-2) : 
            c = a + b 
            a = b 
            b = c 
            print(c, end = " ")
        print()

fib(10)
fib(1)
fib(2)
fib(20)