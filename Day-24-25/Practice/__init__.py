class Student:
    college_name = "ABC"
    def __init__(self,fullname):

        self.name=fullname;
        print(self)
    def welcome(self):
        print("Welcome ",self.college_name)

s1=Student("Niharika Shetty")
print(s1)
print(s1.name)
s1.welcome()



s2=Student("Niriksha ")
print(s2.name)
print(s2.college_name)
