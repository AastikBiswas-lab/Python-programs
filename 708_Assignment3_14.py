def flatten_list(list1):
    list2 = []
    
    for i in list1:
        if i == []:
            print()
        elif i == [i]:
            list2.append(i)
        else:
            if type(i) == list:
                list2 += flatten_list(i)
            else:
                list2.append(i)
    
    return list2
a = int(input("Enter the size of the main list : "))
list1 = []
list2 = []
b = int(input("Enter the size of the sublist : "))
for i in range(a):
    print("Enter the elements of the sublist ",(i+1),": ")
    for j in range(b):
        c = int(input())
        list2.append(c)
    list1.append(list2)
    list2 = []
print("The original list is : ", list1)
print("Flattened list:", flatten_list(list1))