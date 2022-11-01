
import random
print(" Number Guessing Game \n\n")
print("You have 4 chances to try a number for easy level and 7 chances for easy and hard level\n\n")



def gaming(a,b,chances):
    num = random.randint(a,b)
    chance = 0
    while (chance<chances):
        guess = int(input(f"\n Enter number between {a} and {b} \n"))
        chance+=1
        if guess == num:
            print('\n Great! you guessed it correctly \n')
            break
        elif (guess >= b) or (guess <= a):
            print('\n Wrong input! Entered number is out of limits \n')
    else:
        print(f"\n You tried {chances} chances Better Luck Next Time \n")
        
def game_level():
    level = input('Which level of game you want to play: Easy/Medium/Hard ').lower()
    if level == 'easy':
        gaming(0,10,4)
    elif level== 'medium':
        gaming(0,20,7)
    elif level == 'hard':
        gaming(0,30,7)
    else:
        print('Invalid Input')
game_level()