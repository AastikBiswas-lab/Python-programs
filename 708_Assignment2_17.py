a = int(input("Enter the size of the  the list: "))
list1 = []
print("Enter the elements of the list: ")
for i in range(a):
    b = input()
    list1.append(b)
for i,j in enumerate(list1):
    print("position: ",i,"element: ",j)