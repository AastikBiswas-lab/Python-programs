def prod(list1):
    if len(list1) == 0:
        return 1
    return list1[0] * prod(list1[1:])
a = int(input("Enter the number of elements in the list: "))
list1 = []
for i in range(a):
    list1.append(int(input("Enter element: ")))
print("Product:", prod(list1))