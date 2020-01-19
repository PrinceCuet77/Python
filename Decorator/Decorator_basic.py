def square(a) : 
    return a**2 

new_square = square 
print(new_square(7))
print(square(7))

print(new_square.__name__)
print(square.__name__)

print(square)
print(new_square)

# Function as argument
def square(a) : 
    return a ** 2 

def my_map(function, l) :                                   # Custom funciton which takes function as parameter
    new_list = [] 
    for item in l : 
        new_list.append(function(item))
    return new_list
    
l = [i for i in range(1, 6)]
print(my_map(square, l))

# Using lambda expression taking function as argument
print(my_map(lambda a : a ** 3, l))

# Function returning function -- Closure
# Method : 01 (Most preferable)
def outer_function() : 
    def inner_function() : 
        print('Inside the inner function')
    return inner_function

outside_function = outer_function()
outside_function()
print()

# Method : 02 
def outer_function2() : 
    def inner_function2() : 
        print('Inside the inner function 2') 
    return inner_function2()

outside_function2 = outer_function2()

# Example : 01 
def outer_function3(msg) : 
    def inner_function3() : 
        print(f'Message is : {msg}')
    return inner_function3

outside_function3 = outer_function3('I am learning python')
outside_function3()

# Example : 02 
def to_power(x) : 
    def cal_power(n) : 
        return n ** x 
    return cal_power

square = to_power(2)
print(square(2))

cube = to_power(3)
print(cube(2))

# Learn Decorator 
# Step : 01 
# Decorator - enhance the functionality of others functions

def decorator_function(function) : 
    def wrapper_function() : 
        print('This is awesome function')
        function()
    return wrapper_function

@decorator_function
def func() : 
    print('This is another function')

func()

# Step : 02
def decorator_function(function) :
    def wrapper_function(*args, **kwargs) : 
        print('This is awesome function') 
        return function(*args, **kwargs)                # Writing 'return' means that it works both add(2, 3) and func()
    return wrapper_function

@decorator_function 
def func(a) : 
    print(f'this is another function {a}') 

func(5)

@decorator_function
def add(a, b) : 
    return a + b 

print(add(2, 3))

# Step : 03
from functools import wraps

def decorator_function(function) :
    @wraps(function)                            # Otherwise func.__name__ shows wrapper_function 
    def wrapper_function(*args, **kwargs) : 
        '''This is wrapper function message'''
        return function(*args, **kwargs)
    return wrapper_function

@decorator_function 
def func() : 
    '''This is func function message''' 

print(func.__doc__)
print(func.__name__)

# Example : 02
# To print: 
# You are calling add function
# This funciton takes two arguments and returning their sum
# 9

from functools import wraps 

def print_function_data(function) : 
    @wraps(function)
    def wrapper_function(*args, **kwargs) : 
        print(f'You are calling {function.__name__} function')
        print(f'{function.__doc__}')
        return function(*args, **kwargs)
    return wrapper_function

@print_function_data 
def add(a, b) : 
    '''This funciton takes two arguments and returning their sum'''
    return a + b 

print(add(4, 5))

# Example : 03
# Calculating time 
from functools import wraps 
import time 

def decorator_function(function) : 
    @wraps(function)
    def wrapper_function(*args, **kwargs) : 
        t1 = time.time()
        returned_value = function(*args, **kwargs) 
        t2 = time.time()
        print(f'time : {t2-t1}') 
        return returned_value 
    return wrapper_function

@decorator_function 
def func() : 
    new_list = [] 
    for i in range(1, 10000) : 
        new_list.append(i**2)
    
func()

# Example : 04 
# Finding sum of the numbers 

from functools import wraps 

def decorator_function(function) : 
    @wraps(function) 
    def wrapper_function(*args, **kwargs) :
        if all(type(arg) == int for arg in args) : 
            return function(*args, **kwargs)
        else : 
            print('Invalid List')

        # new_list = [] 
        # for arg in args : 
        #     new_list.append(type(arg) == int)
        # if all(new_list) : 
        #     return function(*args, **kwargs)
        # else : 
        #     return 'Invalid List'                 # Most preferable
    return wrapper_function

@decorator_function
def checking(*args) : 
    total = 0
    for i in args : 
        total += i
    return total 

print(checking(1, 2, 3, 4, 5, [1, 2]))
print(checking(1, 2, 3, 4, 5))    

# Decorator with argument

from functools import wraps 

def chosing_data_type(data_type) : 
    def decorator_function(function) : 
        @wraps(function) 
        def wrapper(*args, **kwargs) : 
            if all(type(arg) == data_type for arg in args) : 
                return function(*args, **kwargs)
            else : 
                return 'Invalid'
        return wrapper
    return decorator_function

@chosing_data_type(str)
def checking(*args) : 
    total = ''
    for i in args : 
        total += i
    return total 

print(checking('Rezoan', ' ', 'Shakil'))
print(checking('Rezoan', 77))