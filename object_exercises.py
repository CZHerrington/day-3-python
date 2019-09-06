# OOP Exercises 1

class Person: 
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print('contact info:\nphone: {}\nemail: {}'.format(self.phone, self.name))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info()
jordan.print_contact_info()

# OOP Exercises 2

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("{} {} {}".format(self.make, self.model, self.year))

car = Vehicle('Honda', 'Civic', '2016')
car.print_info()

