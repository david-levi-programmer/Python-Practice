class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Woof!")


class Cat(Mammal):
    def meow(self):
        print("Meow.")


sunny = Dog()
sunny.walk()
sunny.bark()
thomas = Cat()
thomas.walk()
thomas.meow()
