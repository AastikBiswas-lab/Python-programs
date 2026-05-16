def generator(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return generator(n-1)+generator(n-2)
n=int(input("Enter the value of N: "))
for i in range(n):
    print(generator(i))