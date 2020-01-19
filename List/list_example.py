# Given a list and generate the square of the list's element : [1, 2, 3] -> [1, 4, 9]
def sqrt(l) : 
    sq = [] 
    for i in l : 
        sq.append(i*i)                              # Or : sq.append(i**2)
    return sq 

l = list(range(1, 6))
print(sqrt(l))

# Print a list in reverse order : [1, 2, 3] -> [3, 2, 1]
def revUsingReverseFunction(l) :                                    # Using reverse() function
    l.reverse()
    return l

def revUsingSlicing(l) :                                            # Using string slicing 
    return l[::-1]

def revUsingPop(l) :                                                # Using pop() funtion
    revL = [] 
    for i in range(len(l)) : 
        item = l.pop()
        revL.append(item)
    return revL 

l = list(range(1, 6))

lt = l.copy()
lt = revUsingReverseFunction(lt)
print(lt)
print(revUsingSlicing(l))
print(revUsingPop(l))

# Reverse list element : ['abc', 'tuv', 'xyz'] -> ['cba', 'vut', 'zyx']
def rev(l) :
    revL = [] 
    for i in l : 
        revL.append(i[::-1])
    return revL 

l = ['abc', 'tuv', 'xyz']
print(rev(l))

# [odd, even] : [1, 2, 3, 4, 5] -> [[1, 3, 5], [2, 4]]
def func(l) : 
    odd = []
    even = []
    for i in l : 
        if ( i % 2 == 0 ) : 
            even.append(i) 
        else : 
            odd.append(i)
    res = []
    res.append(odd)
    res.append(even)
    return res 

l = [1, 2, 3, 4, 5]
print(func(l))

# [1, 2, 3, 4] & [1, 2, 5, 6] -> [1, 2]
def func(l1, l2) : 
    res = []
    for item in l1 : 
        if item in l2 : 
            res.append(item)
    return res 

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]
print(func(l1, l2))

# Finding how many list into the list : [1, 2, 3, [1, 2], [3, 4], []] -> 3
def func(l) :
    cnt = 0
    for i in l : 
        if type(i) == list : 
            cnt += 1
    return cnt 

l = [1, 2, 3, [1, 2], [3, 4], []]
print(func(l))