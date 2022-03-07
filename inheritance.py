class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("i am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal): #inheritance
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):   #create new methods
            print("woof!")

    def who_am_i(self):
        print("i am a dog")   #rewrite or ovrride

mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()

myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()
