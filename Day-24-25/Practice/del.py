class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marksofStudent=marks

s1=Student("Niharika Shetty",89)
print(s1.name)
print(s1.marksofStudent)
del s1.name
# print(s1.name)
print(s1.marksofStudent)
