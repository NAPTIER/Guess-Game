#Guess Game
import random
n=random.randint(1,100)
print("Guess the no. between 1 and 100 in 9 attempts: ")
i=1
a = int(input("Enter the Guess: "))
while(i<9):
    a1=9-i
    if a==n:
        print("YOU WON")
        break
    elif a>n:
        print("Try with a smaller no.")
        print("Attempts left: ",a1)
        a = int(input("Enter the Guess: "))
    else:
        print("Try with a bigger no.")
        print("Attempts left: ",a1)
        a = int(input("Enter the Guess: "))
    i=i+1
if i>9:
    print("BETTER LUCK NEXT TIME")


