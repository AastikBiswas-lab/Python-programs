def union(s1,s2):
    s3 = set()
    s3 = s1.union(s2)
    return s3
def intersection(s1,s2):
    s3 = set()
    s3 = s1.intersection(s2)
    return s3
def difference(s1,s2):
    s3 = set()
    s3 = s1.difference(s2)
    return s3
def symm_diff(s1,s2):
    s3 = set()
    s3 = s1.symmetric_difference(s2)
    return s3
def subset(s1,s2):
    if s1.issubset(s2):
        print("set 1 is a  subset of set 2")
    else:
        print("set 1 is not a subset of set 2")
def superset(s1,s2):
    if s1.issuperset(s2):
        print("set 1 is a  superset of set 2")
    else:
        print("set 1 is not a superset of set 2")
def count(s1):
    return len(s1)
def check(s1,n):
    if n in s1:
        print(n,"is present in the set")
    else:
        print(n,"is not present in the set")
def power_set(a):
    n = len(a)
    for i in range(2 ** n):
        list3 = []
        temp = i   
        for j in range(n):
            if temp % 2 == 1:
                list3.append(a[j])
            temp = temp // 2   
        print(list3)
a = int(input("Enter the size of set 1: "))
b = int(input("Enter the size of set 2: "))
s1 = set()
list1 = []
s2 = set()
list2 = []
print("Enter the elements of set 1: ")
for i in range(a):
    list1.append(int(input()))
print("Enter the elements of set 2: ")
for i in range(b):
    list2.append(int(input()))
s1 = set(list1)
s2 = set(list2)
n = int(input("Enter a number to check if it is present in set 1: "))
check(s1,n)
n = int(input("Enter a number to check if it is present in set 2: "))
check(s2,n)
n = int(input("Enter the size of the list : "))
list3 = []
print("Enter the elements of the list: ")
for i in range(n):
    list3.append(int(input()))
set3 = set(list3)
print("Union of set 1 and set 2 is: ",union(s1,s2))
print("Intersection of set 1 and set 2 is: ",intersection(s1,s2))
print("Difference of set 1 and set 2 is: ",difference(s1,s2))
print("Symmetric difference of set 1 and set 2 is: ",symm_diff(s1,s2))
subset(s1,s2)
superset(s1,s2)
print("Set after removing duplicates is: ",set3)
print("Number of elements in set 1 is: ",count(s1))
print("Number of elements in set 2 is: ",count(s2))
print("Power set of set 1 is: ")
power_set(list1)
print("Power set of set 2 is: ")
power_set(list2)
