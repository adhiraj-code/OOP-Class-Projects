class Dog:
    #private class attribute
    __species = "Pug"

    def __init__(self, name, color):
        self.name = name
        self.color = color

obj = Dog("Tommy", "Grey White")
print(obj.name)
print(obj.color)
print(obj.species)
