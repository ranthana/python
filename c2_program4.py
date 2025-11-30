start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Four-digit numbers with all even digits and perfect square:")

for num in range(start, end + 1):
    if 1000 <= num <= 9999:  
        if str(num).isdigit() and all(int(d) % 2 == 0 for d in str(num)):
            
            if int(num**0.5) ** 2 == num:
                print(num)
