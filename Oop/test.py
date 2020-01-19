# ----------------------------  Class details ------------------------------------------
class Person :                                                # Convension : Class name's first letter is capital.
    def __init__(self, first_name, last_name, age) : 
        print('Init method or constructor method') 
        # Instance variables
        # Object(self).Instance Variable(first_name) = Local Variable(first_name)
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age 

    def full_name(self) : 
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self) : 
        return self.age > 18

p1 = Person('Rezoan', 'Shakil', 22)

print(f'First name : {p1.first_name}')
print(f'Last name : {p1.last_name}')
print(f'Age : {p1.age}')
print()
print(p1.full_name())
print(p1.is_above_18())

# ------------------------------ Class variable ----------------------------------------------- 
class Circle : 
    pi = 3.1416                                                 # Class variable or class attribute
    def __init__(self, radius) : 
        self.radius = radius 
    
    def calculate_circumference(self) : 
        return Circle.pi * self.radius * self.radius            # Class Name(Circle).Class Variable(pi) 

c1 = Circle(4)
print(c1.__dict__)                                              # The overview of all the variables in dictionary
print(c1.calculate_circumference())

# ----------------------------- Example : 01 ------------------------------------------------- 
# Counting total objects of the class

class Person2 : 
    count_instance = 0 
    def __init__(self) : 
        Person2.count_instance += 1

    @classmethod                                                  # Class method using decorator
    def total_instances(cls) :                                    # 'cls' indicates 'Person2' class
        return f'I have created {cls.count_instance} instances of {cls.__name__} class'

P1 = Person2() 
P2 = Person2()
print(Person2.count_instance)
print(Person2.total_instances())

# ------------------------------ Class method as a constructor and static method -----------------------------
class Person3 : 
    def __init__(self, first_name, last_name, age) : 
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age

    @classmethod 
    def from_string(cls, string) : 
        first_name, last_name, age = string.split(',') 
        return cls(first_name, last_name, age)

    @staticmethod 
    def hello() :                                                   # Static method 
        print('Hello, Static method called')

# Own made object created by class method
P3 = Person3.from_string('Rezoan,Shakil,22')
print(f'First name : {P3.first_name}')
print(f'Last name : {P3.last_name}')
print(f'Age : {P3.age}')
print()

Person3.hello()