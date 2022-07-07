
# Online IDE - Code Editor, Compiler, Interpreter
import random as r

beg=int(input("Let's generate a random number! Please enter the floor of your range."))
end=int(input("Great! What should the ceiling be?"))
print('Thanks! I\'m thinking....')
num=r.randrange(beg,end,)
print(f'Your random number is {num}. Thanks for playing!')

