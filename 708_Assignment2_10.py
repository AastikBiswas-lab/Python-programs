a = int(input("Enter the size of the list : "))
list1 = []

count = 0
list3 = []
print("Enter the elements of the list : ")
for i in range(a):
    a = int(input())
    list1.append(a)
for i in range(len(list1)):
    if list1[i] not in list1[:i]:
     for j in range(i , len(list1)):
        if list1[i]==list1[j]:
            count = count +1
    
    
     list3.append((list1[i], count))
    count = 0
print( list3)
            