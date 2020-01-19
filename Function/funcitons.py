def add(n1, n2) : 
    return n1 + n2                                          # Returning value

n1 = int(input("First number : "))
n2 = int(input("Second number : "))
print(add(n1, n2))

def printable(message) : 
    print(f"printable says : {message}")

printable("My name is Prince")

# Default parameter 
def func(firstName = "unknown", lastName = "unknown", age = None) :
    print(f"First name : {firstName}")
    print(f"Last name : {lastName}")
    print(f"Age : {age}")

func(), print()
func("Rezoan"), print()
func("Rezoan", "Shakil"), print()
func("Rezoan", "Shakil", 22)