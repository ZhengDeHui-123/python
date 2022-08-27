
class Person:
    age = 10
    def __init__(self):
        age = self.age


person = Person()
print(person.age)
person.age=20
print(person.age)
