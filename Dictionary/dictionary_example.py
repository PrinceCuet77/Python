# Example : 01 
# {1:1, 2:8, 3:27} 
def cube_finder(value) : 
    d = {} 
    for i in range(1, value+1) : 
        d[i] = i ** 3
    return d 

print(cube_finder(3))

# Example : 02 
# How many character have in the string 
# Word counter 
def word_counter(word) : 
    d = {} 
    for i in range(len(word)) : 
        if word[i] not in d : 
            d[word[i]] = word.count(word[i])
    return d

# def word_counter(word) : 
#     d = {} 
#     for ch in word : 
#             d[ch] = word.count(ch)
#     return d

word = "HaRsHiT vaShItHa" 
di = word_counter(word) 
print(di)

word = "Harshit Vashitha" 
di = word_counter(word) 
print(di)

# Example : 03 
# Taking input 
name = input("Enter your name : ")
user_info = {}
user_info['name'] = name

age = input("Enter your age : ")
user_info['age'] = age

fav_movies = input("Enter your movies : ").split() 
user_info['fav_movies'] = fav_movies

fav_songs = input("Enter your songs : ").split() 
user_info['fav_songs'] = fav_songs

for key, value in user_info.items() : 
    print(f"{key} : {value}")