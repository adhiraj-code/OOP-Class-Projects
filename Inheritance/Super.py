# Parent Class

class Employee:

    def __init__(self, id, name):

        self.id = id

        self.name = name

# sub class

class email(Employee):

    def __init__(self, email, id, name):

        super().__init__(id, name)

        self.email = email

obj = email(101, "Adhiraj", "adhiraj@gmail.com")

print(obj.id)

print(obj.name)

print(obj.email)