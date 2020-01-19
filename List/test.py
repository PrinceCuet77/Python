

# [odd, even] : [1, 2, 3, 4, 5] -> [[1, 3, 5], [2, 4]]

def fun(l) : 
    odd = []
    even = []
    for i in l : 
        if i % 2 == 0 : 
            odd.append(i)
        else : 
            even.append(i)
    total = [] 
    total.extends(odd) 
    total.extends(even)
    return total

l = [1, 2, 3, 4, 5]
value = fun(l)
print(value)

# [1, 2, 3, 4] & [1, 2, 5, 6] -> [1, 2]
# Finding how many list into the list : [1, 2, 3, [1, 2], [3, 4], []] -> 3