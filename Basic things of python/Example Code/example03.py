import random 
winning_number = random.randint(1, 100) 

time = 0
while True :
    value = int(input("Enter the value : "))
    time += 1

    if value == winning_number : 
        break;
    elif value < winning_number : 
        print("Too short")
    else : 
        print("Too large")

print(f"You win in {time} time(s)")