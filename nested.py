x = 25
def printer():
    x = 50
    return x
print(x)

print(printer())

name = 'THIS IS A GLOBAL STRING'

def greet():
    name = 'Sammy'

    def hello():

        print('Hello '+name)

    hello()
print(greet())

