class Student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Branch:",self.branch)
s1=Student("Apoorva",21,"CSE")
s1.display()