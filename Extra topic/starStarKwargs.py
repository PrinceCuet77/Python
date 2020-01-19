def show(**kwargs) : 
    print(kwargs)
    print(type(kwargs))                                 # Dictionary
    for key, value in kwargs.items() : 
        print(f"{key} : {value}")

show(firstname = 'Rezoan', lastname = 'Shakil')

# **kwargs with normal variable
def show(name, **kwargs) : 
    print(name) 
    print(kwargs)
    for key, value in kwargs.items() : 
        print(f"{key} : {value}") 

show('hello', firstname = 'Rezoan', lastname = 'Shakil')

# Dictionary unpacking
def show(**kwargs) : 
    for key, value in kwargs.items() : 
        print(f"{key} : {value}")

di = {'firstname' : 'Rezoan', 'lastname' : 'Shakil'}
show(**di)                                                  # Unpacking

# PADK
# Parameters
# *args
# Default parameters
# **kwargs

def showAll(message, *args, default_parameters = 'unknown', **kwargs) : 
    print(message)
    print(args) 
    print(default_parameters)
    print(kwargs)

showAll('Hello world', 1, 2, 3, a = 1, b = 2) 

# Example 
# If reverse_str = True then first reverse all the string and capital the first letters otherwise only capital the first letters
def show(name, **kwargs) : 
    if kwargs : 
        return [ch[::-1].title() for ch in name]
    else : 
        return [ch.title() for ch in name]

name = ['rezoan', 'shakil']
print(show(name, reverse_str = True))

print(show(name))