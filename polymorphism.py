class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof"

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow"

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(pet)   #class
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())

print(pet_speak(niko))
print(pet_speak(felix))

class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("subclass must implemented this")

class Dog(Animal):
    def speak(self):
        return self.name+ " says woof"

fido = Dog("Fideo")
isis = Cat("Isis")

print(fido.speak())