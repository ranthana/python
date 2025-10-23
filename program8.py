s=input("enter a string:")
first_char=s[0]
result=first_char
for ch in s[1:]:
    if ch == first_char:
        result += '$'
    else:
        result += ch
        print("result:",result)