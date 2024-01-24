import random
from tkinter import FALSE

def Gamewin(comp, you):
    if comp == you:
        return None

    elif comp == 'rock':
        if you == 'scissor':
            return False
        elif you == 'paper':
            return True

    elif comp == 'scissor':
        if you == 'rock':
            return True
        elif you == 'paper':
            return False

    elif comp == 'paper':
        if you == 'scissor':
            return True
        elif you == 'rock':
            return False

    elif comp == 'scissor':
        if you == 'paper':
            return False
        elif you == 'rock':
            return True

    elif comp == 'rock':
        if you == 'paper':
            return True
        elif you == 'scissor':
            return False

    elif comp == 'paper':
        if you == 'rock':
            return False
        elif you == 'scissor':
            return True


print("Computer's Turn: Rock(r), Paper(p), Scissor(s) ?")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 'rock'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'scissor'

you = input("Your's Turn: Rock(r), Paper(p), Scissor(s) ?\n")

a = Gamewin(comp, you)

print(f"Computer Choose {comp}")
print(f"Your Choose {you}")

if a == None:
    print("The Game is Tie!!!")
elif a:
    print("Yoy Win!!!")
else:
    print("You Lose!!!")