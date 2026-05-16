a = int(input("Enter the size of the tupple : "))
t1 = ()
list1 = []
print("Enter the elements of the tupple : ")
for i in range(a):
    a = int(input())
    list1.append(a)
t1 = tuple(list1)
for i in range(len(t1)):
    if t1[i] % 2 == 0:
        print(t1[i])