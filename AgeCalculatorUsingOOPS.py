import datetime
class Student:
    age=20
    print("student of ITS")



x=Student()
print(x.age)

class AgeCalculator:
    def agefinder(c_year ,b_year):
        age=c_year - b_year
        print("your age is { }".format(age))



x=AgeCalculator()
b_year=int(input("enter your birth year = "))
c_year=int(input("enter current year = "))
x.agefinder(c_year,b_year)

     
