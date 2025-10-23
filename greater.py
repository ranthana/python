n=input("enter a list of integer seperte by space").split()
result=[int(num)if int (num)<=100
        else"large" for num in n]
print("Numbers:",result)

