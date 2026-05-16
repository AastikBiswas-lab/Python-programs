def reverse_num(n, rev):
    if n == 0:
        return rev
    else :
        rev = rev * 10 + (n % 10)
        return reverse_num(n // 10, rev)
num = int(input("Enter a number: "))
rev = reverse_num(num, 0)
if num == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")