# super class

class Vehicles:

# Constructor

    def __init__(vehicleType):

        print('Vehicles is a ', vehicleType)

# sub class

class Car(Vehicles):

# Constructor

    def __init__(self):

        Vehicles.__init__('Car')

# Driver's code

print(issubclass(Car, Vehicles))