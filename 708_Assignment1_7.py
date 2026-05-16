import re
password = input("Enter your password: ")
l = len(password)
count = 0
if l>=8:
    count+=1
    upper = re.compile(r"[A-Z]+")
    if upper.search(password):
        count+=1
    else :
        print("Password must contain at least one uppercase letter.")
        
    lower = re.compile(r"[a-z]+")
    if lower.search(password):
        count+=1
    else :
        print("Password must contain at least one lowercase letter.")
        
    digit = re.compile(r"[0-9]+")
    if digit.search(password):
        count+=1
    else :
        print("Password must contain at least one digit.")
    special = re.compile(r"[!@#$%^&*]+")
    if special.search(password):
        count+=1
    else :
        print("Password must contain at least one special character.")
else :
    print("Password must be at least 8 characters long.")
if count < 3:
    print("WEAK")
elif count <5:
    print("MODERATE")
else:
    print("STRONG")