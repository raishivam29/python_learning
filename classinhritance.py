class Animal():
    def speak(self):
        print("animal can speak")
class Dog(Animal):
    def bark(self):
        print("dog can bark")
class Babydog(Dog):
    def eat(self):
        print("baby dog eat only milk ")
d=Babydog()
d.speak()
d.bark()
d.eat()
