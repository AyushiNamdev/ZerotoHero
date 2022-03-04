def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2 ==0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['andy', 'even', 'cherrys']
print(list(map(splicer,names)))

def check_even(num):
    return num%2 == 0
my_nums = [1,2,3,4,5,6]

for n in filter(check_even,my_nums):
    print(n)


def square(num):
    result = num **2
    return result

(square(3)) #use print to print it

square = lambda num: num ** 2 #lambda expression
print(square(5))

print(list(map(lambda num:num**2,my_nums)))

def check_even2(num):
    return num%2 == 0

a = list(filter(lambda num: num%2 ==0,my_nums))
print(a) 