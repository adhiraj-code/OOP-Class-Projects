class flowers:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def __del__(self):
        print("destructor called")

obj = flowers("lotus", "pink")
print(obj.name)
print(obj.colour)

del obj