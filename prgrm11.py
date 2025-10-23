a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
if a>=b and a>=c:
    print("biggest number is:",a)
elif b>=a and b>=c:
    print("biggest number is",a)
else:
    print("biggest number is:",c)
