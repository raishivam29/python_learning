class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.age)

    # def __add__(self, obj):
    #     return self.id + obj.id

class presentation:
    p1 = Person(1, 'satish', 23)
    p2 = Person(2, "Shivam", 23)
    print(p1)
    print(p2)

    try:
        print(p1 + p2)
    except Exception as ex:
        print("kaha /")

    print("Program executed successfully!")
    
# class Teacher(Person):
#     pass

# class Student(Person):
#     pass

print(1 + 2)
print("a" + '1')