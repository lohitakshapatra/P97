import random
print("Number guessing game")
number=random.randint(1,9)
chances=0
while chances<5:
    guess=int(input("Enter your guess : "))
    if guess ==number:
        print("congratulations u won")
        break
    elif guess<number:
        print("your guess was too low")    
    else :
        print("your guess is too high")  
    chances+=1
if chances==5:
    print  ("you lose")      
