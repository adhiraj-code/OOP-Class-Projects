class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("My Dog's Name is ", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

obj = Dog("Jimmy")
obj.info()
obj.sound()