a = int(input("Enter the size of the list : "))
list1 = []
print("Enter the elements of the list : ")
for i in range(a):
    a = int(input())
    list1.append(a)
list2 = []
list2 = list1[::-1]
print("The reversed list is : ", list2)