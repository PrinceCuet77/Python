# any() and all() function
# any() function check if any of them is true then show true otherwise false
# all() function check if all of them is true then show true otherwise false

number1 = [2, 4, 6, 8, 10]
number2 = [2, 3, 4, 6, 10]
number3 = [1, 3, 5, 7, 9]

print(all([n % 2 == 0 for n in number1]))
print(all([n % 2 == 0 for n in number2]))
print()

print(any([n % 2 == 0 for n in number2]))
print(any([n % 2 == 0 for n in number3]))
print()

# Example : 01 
# Finding the total of the lists which contains numbers.If list contains string then return 'Wrong input'

def finding_sum(*args) : 
    if all([(type(value) == int or type(value) == float) for value in args]) : 
        total = 0
        for val in args : 
            total += val
        print(f'Total : {total}')
    else : 
        print('Wrong input')

finding_sum(1, 2, 3, 4, 5.0, 'Prince', ['Prince77', 77, 77.0])
finding_sum(1, 2, 3, 4, 5.0)