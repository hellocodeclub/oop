class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print('Hello! My name is '+ self.name)
    def say_age(self):
        print('My age is'+str(self.age))

person1 = Person('Mickey',30)
person1.say_hello()
person1.say_age()




