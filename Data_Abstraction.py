
"""Abstraction in python is defined as a process of
handling complexity by hiding unnecessary information from the user"""
#access == abstraction

class ineuron:
    __students ="data science"  #private variable

    def students(self):
        print("print the class of students",ineuron.__students)

i= ineuron()
i.students()
i._ineuron__students
#this is the data that is hidden if we have to access it first we have to go to class then only access it

class rexa:
    def __init__(self):
        self.sam1="data analyst"

    def sam(self):
        print(self.sam1)

x=rexa()
x.sam()
x.sam1="Data science" #over riding the variable 
x.sam()


