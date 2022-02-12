import random 
print('Number Guessing Game')
randomNumber= random.randint(1,9)
chances=0
print('Guess number between 1-9')
while (chances<5):
    inputUser = int(input('enter the guess: '))
    if(inputUser== randomNumber):
        print('Congrats you won')
        break
    elif(inputUser<randomNumber):
        print('Guess higher than: ',inputUser)
    else:
        print('Guess lower than: ',inputUser)
    chances=chances+1

if (chances == 4):
    print('You lost game,the number was',randomNumber)

