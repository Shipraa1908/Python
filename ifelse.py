age = int(input("enter your age = "))
gender=input("enter your gender M/F = ")
if (age>17):
    if gender=="F":
        print("eligible for govt job")
    elif(gender=="M"):
         print("eligible for pvt job")
    else:
        print("inappropriate gender")
else:
    print("u r underage")             
