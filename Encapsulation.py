
"""Concept of encapsulation says that we are not suppose to allow a user
to modify a value of variable directly then you can achieve encapsulation"""
#modification == encapsulation

class ineuron1:
    def __init__(self):
        self.__students1 = "data Scientist"

    def students(self):
        print(self.__students1)

    def student_change(self): #it can be called as setter function as we are setting a (private) variable or changing it
        self.__students1 ="big data by me"

#if you have to reassign a value for private var you need to do it with the help of class method itself
#directly you will not be able to change it or override it

    def student_change_direct(self,new_value):
        self.__students1 =new_value

s=ineuron1()
s.students()
"""s.__students1="big data"
s.students()"""
s.student_change()
s.student_change_direct("sohail") #it will override this data as well
s.students()

