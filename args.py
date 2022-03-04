def myfunc(a,b,c = 0):
    # returns 5% of the sum of a and b
    return sum((a,b,c)) *0.05

print(myfunc(40,60,100))

def myfunct(*args):
    print(args)
    return sum(args) * 0.05
myfunct(40,60)
print(myfunc(40,60))



