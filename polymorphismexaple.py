class Cat:
    def __init__(self,name1,age1):
        self.name=name1
        self.age=age1

    def info(self):
        print(f"my name is {self.name}. I am {self.age} year old")

    def sound(self):
        print("meao")

class Dog:
    def __init__(self,name1,age1):
        self.name=name1
        self.age=age1

    def info(self):
        print(f"My name is {self.name}.I am {self.age} year old")

    def sound(self):
        print("bark")

Cat1=Cat("kitty",2.4)
dog1=Dog("rambo",7)
for animal in (Cat1,dog1):
    animal.sound()
    animal.info()
    animal.sound()