a = int(input("Enter the size of the list : "))
list1 = []
print("Enter the elements of the list : ")
for i in range(a):
    a = int(input())
    list1.append(a)
sum = 0
for i in range(len(list1)):
    sum += list1[i]
print("The sum of the elements in the list is : ", sum)