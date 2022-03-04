example = [1,2,3,4,5,6,7]
from random import shuffle

result = shuffle(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)

print(result)

mylist = [' ', 'O', ' ']
shuffle_list(mylist)

print(shuffle_list(mylist))

def player_guess():
    guess= ''

    while guess not in ['0', '1', '2']:
        guess = input('pick a number: 0, 1, 2')
    return int(guess)
print(player_guess())
myindex = player_guess()

def check_guess(mylist,guess):
    if mylist[guess] == 0:
        print("correct")
    else:
        print("wrong guess")
        print(mylist)




