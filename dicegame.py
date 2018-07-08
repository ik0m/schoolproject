import random
print('What is your name?')
x=input('> ')
print('Hello, ',x,'!',sep='')
d1=random.randint(1,6)
d2=random.randint(1,6)
print('Rolling the dice...\nDie 1: ',d1,'\nDie 2: ',d2,'\nTotal value: ',d1+d2)
if d1+d2>7:
    print('You won.')
else :
    print('You lost')
