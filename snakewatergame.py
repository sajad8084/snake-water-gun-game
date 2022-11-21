import random
import re

def game(comp, me):
    if comp==me:
        return f"Draw Game"
    if comp=='s':
        if me=='w':
            return False
        elif me=='g':
            return True
    elif comp=='w':
        if me=='g':
            return False
        elif me=='s':
            return True
    elif comp=='g':
        if me=='s':
            return False
        elif me=='w':
            return True


randomNo = random.randint(1,3)
if randomNo==1:
    comp='s'
elif randomNo==2:
    comp='w'
elif randomNo==1:
    comp='g'


me=input("My Turn, I can choose snake(s) water(w ) or gun(g) ")

g=game(comp,me)

print(f"Pc Chose {comp} ")
print(f"I Chose {me} ")

if comp==me:
    print("Draw Game")
elif g:
    print("You Won The Game")
else:
    print("You Lost")