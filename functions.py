#def name_of_function(): it uses snake casing that i s all underscore and lower case

def say_hello():
    print("Hello")
    print("how are")
    print("you")

say_hello()

def say_hi(name = 'default'):
    print(f'Hello {name}')

say_hi()

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

print_result(10,4)