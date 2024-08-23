myList = [1, 5, 8, 11, 20]
guesses =[]
points=0
while len(guesses) < 5:
    num = int(input("Pick a number from 1-20: "))
    if num in guesses:
        print("You already gussed that!")
        guesses.append(num)

    elif num in myList:
        print("Good!")
        guesses.append(num)
        points=points + 1
        
    elif num not in myList:
        print("Try again!")
        guesses.append(num)
    

print("You guessed: " + str(guesses))
print("My numbers were " + str(myList))
print("Points: " +str(points))


# This a game of Guess the Number , you have 5 tires to guess 5 numbers .
#For each number you get correct , you get 1 point .
#At the end the correct numbers will be revealed and your points.
#Tip : Make sure you don't guess the same number again !
