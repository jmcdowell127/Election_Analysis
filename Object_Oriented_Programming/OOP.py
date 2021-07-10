class Dog:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def bark(self):
        return self.sound + ' ' + self.sound
first_dog = Dog('Fido', 'brown', 'woof!')
print(    first_dog.name)
print(first_dog.color)
first_dog.bark()

second_dog = Dog('Lady', 'blonde', 'arf!')
print(     second_dog.name)
print(second_dog.color)
second_dog.bark()

class Cat:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def meow(self):
        return self.sound + ' ' + self.sound

first_cat = Cat('Felix', 'purrr')
print(first_cat.name)
first_cat.meow()

second_cat = Cat('Garfield', 'lasagna')
print(second_cat.name)
second_cat.meow()