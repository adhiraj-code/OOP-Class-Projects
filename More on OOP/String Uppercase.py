# create class

class IOString():


# constructor to see default value

    def __init__(self):

        self.strl=""


# method to get input from user

    def get_string(self):

        self.strl = input("Enter string : ")

# method to print the string in upper case

    def print_string(self):

        print("Result : ", self.strl.upper())

# Object creation

obj = IOString()

# call function

obj.get_string()

obj.print_string()