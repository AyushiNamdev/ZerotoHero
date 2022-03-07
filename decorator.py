def func():
    return 1
func()

def hello():
    return "Hello"

print(hello())
greet = hello()


def hello(name= 'Jose'):
    print("the hello() function has been executed")

    def greet():
        return "\t this is the great()fucntion insie hello"

    def welcome():
        return "\t this is welcome() inside the hello"
    print(welcome())
print(hello())

