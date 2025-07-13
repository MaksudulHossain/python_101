class Animal:
    def __init__(self):
        print("Animal created")
    def bark(self):
        print("animal bark")

class Dog(Animal):
    def bark(self):
        print("dog class")
    
    def new_bark(self):
        super().bark()

dog = Dog()
dog.bark()
dog.new_bark()
