def dec_to_binary(n):
    if n == 0:
        return
    dec_to_binary(n // 2)
    print(n % 2, end="")

n = int(input("Enter number: "))
if n == 0:
    print("0")
else:
    dec_to_binary(n)