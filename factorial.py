def factorial(n):
    if n==0:
        return 0
    elif n==1 :
        return 1
    else:
        return n*factorial(n-1) 
    
    
a=int(input("enter number to get factorial = "))
b=factorial(a)
print("factorial of {c1} is {c2}".format(c1=a, c2=b))
    