a = int(input("Enter the size of the dictionary : "))
dict1 = {}
list1 = []
list2 = []
for i in range(a):
    k = input("Enter the key : ")
    v = int(input("Enter the value : "))
    list1.append(k)
    list2.append(v)
dict1 = dict(zip(list1, list2))
print("The original dictionary is : ", dict1)
dict2 = {}
dict2 = dict(zip(list2, list1))
print("The swapped dictionary is : ", dict2)