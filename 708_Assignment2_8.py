a = int(input("Enter the size of the list : "))
list1 = []
list2 = []
count = 0
print("Enter the elements of the list : ")
for i in range(a):
    a = int(input())
    list1.append(a)
for i in range(len(list1)):
    if list1[i] not in list1[:i]:
     for j in range(i + 1, len(list1)):
        if list1[i]==list1[j]:
            count = count +1
    if count == 0:
        list2.append(list1[i])
    count = 0
print("The list after removing duplicates is : ", list2)
            