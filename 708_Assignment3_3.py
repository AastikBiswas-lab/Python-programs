def count(n):
    if n == 0:
        return 0
    return 1 + count(n // 10)

num = int(input("Enter number: "))
print("No. of Digits:", count(num))
