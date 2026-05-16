a = int(input("Enter the size of the list : "))
list1 = []
print("Enter the elements of the list : ")
for i in range(a):
    a = int(input())
    list1.append(a)
max1 = max(list1)
print("The maximum element in the list is : ", max1)
min1 = min(list1)
print("The minimum element in the list is : ", min1)
