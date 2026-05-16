def find_max(list1):
    if len(list1) == 1:
        return list1[0]
    m = find_max(list1[1:])
    if list1[0] > m :
        return list1[0]
    else:
        return m
a = int(input("Enter the number of elements in the list: "))
list1 = []
print("Enter elements : ")
for i in range(a):
    b = int(input())
    list1.append(b)
max1 = find_max(list1)
print("The maximum value in the list is:", max1)

