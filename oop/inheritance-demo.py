class Animal:
    type = "animal";
    def __init__(self, breed):
        print(Animal.type + ": " + breed)


class Cat(Animal):
    sound = "meow";
    # child class has constructor -> priority higher than parent
    def __init__(self, breed):
        Animal.__init__(self, breed) # invoke parent constructor
    def talk(self):
        return self.type + ": " + self.sound

cat = Cat("cat")

