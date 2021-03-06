class Animal(object):
    pass


class Dog(Animal):

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def __init__(self, name):
        self.name = name


class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None
        self.hasTail = "false"


class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover

# here I access hasTail variable from person type in frank object
print "%r \n%r \n%r" % (frank.hasTail, mary.pet.name, frank.pet.name)
