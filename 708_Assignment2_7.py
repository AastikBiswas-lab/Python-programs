a = int(input("Enter the size of the list : "))
list1 = []
list2 = []
print("Enter the elements of the list : ")
for i in range(a):
    a = int(input())
    list1.append(a)
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        list2.append(list1[i])
print("The even numbers in the list are : ")
for i in list2:
    print(i)