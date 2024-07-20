import random

n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    a = int(input("Guess a number: "))
    if(a > n):
        print("Lower Number !!!")
        guesses+=1
    elif(a < n):
        print("Higher Number !!!")
    guesses+=1
    

print(f"You have guessed the number {n} perfectly in {guesses} attempt")