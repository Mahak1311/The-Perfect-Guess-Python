#A program that generates a random number and asks the user to guess it

import random

n = random.randint(1, 100)
 #Using random module to let computer generate a random number on it's own.
a = -1
guesses = 0

while(a != n):
    guesses +=1 #To track attempts
    a = int(input("Guess the number: ")) #To take input from user

    if(a > n):

        print("Lower the number please!")
        
    elif(a < n):

        print("Higher the number please!")
        
print(f"You have gussed the number {n} correctly in {guesses} attempt")    

print("Thank you for playing!!")    
