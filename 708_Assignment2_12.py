set1 = set()
set2 = set()
list1 = []
a= int(input("Enter the size of the set 1: "))
print("Enter the elements of set 1: ")
for i in range(a):
    a = int(input())
    list1.append(a)
set1 = set(list1)
list1 = []
a= int(input("Enter the size of the set 2: "))
print("Enter the elements of set 2: ")
for i in range(a):
    a = int(input())
    list1.append(a)
set2 = set(list1)
print("Union of set 1 and set 2 is: ", set1.union(set2))
print("Intersection of set 1 and set 2 is: ", set1.intersection(set2))
print("Difference of set 1 and set 2 is: ", set1.difference(set2))