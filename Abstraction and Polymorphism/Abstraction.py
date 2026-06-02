# Abstract Base Class

class rectange():

# abstract method

    def area(self):

        pass

# sub class

class calculate(rectange):

    def area(self, length, breadth):

        self.length = length

        self.breadth = breadth

        return self.length * self.breadth

obj = calculate()

print(obj.area(30, 15))