set1 = set()
list1 = []
a= int(input("Enter the size of the set: "))
print("Enter the elements : ")
for i in range(a):
    a = int(input())
    list1.append(a)
set1 = set(list1)
for i in set1:
    print(i,end=" ")