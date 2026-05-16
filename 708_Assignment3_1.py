def check(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return check(s[1:-1])

s = input("Enter string: ")
if check(s)==True:
    print("Palindrome")
else:
    print("Not a palindrome")