filename=input("enter the file name:")
parts=filename.split(".")
if len(parts) > 1:
    print("file extention is:",parts[-1])
else:
    print("no extention found.")


