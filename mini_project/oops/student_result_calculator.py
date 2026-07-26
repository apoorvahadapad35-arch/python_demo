class Student:

 def __init__(self,name,marks):
    self.name=name 
    self.marks=marks
 def result(self):
    if self.marks>=35:
        print(self.name,"Pass")
    else:
        print(self.name,"Fail")
s1=Student("Apoorva",90)
s1.result()

s2=Student("Rohit",25)
s2.result()