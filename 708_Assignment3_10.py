def subsets(s, c, i):
    if i == len(s):
        print(c)
        return
    subsets(s, c + [s[i]], i + 1)
    subsets(s, c, i + 1)
a = int(input("Entersize of the list: "))
s = []
print("Enter the elements of the list:")
for i in range(a):
    b = int(input())
    s.append(b)
subsets(s, [], 0)