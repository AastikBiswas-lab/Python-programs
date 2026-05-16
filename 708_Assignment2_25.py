a = int(input("enter the size of the lists : "))
list1 = []
list2 = []
print("Enter elements for list1:")
for i in range(a):
    n = int(input())
    list1.append(n)
print("Enter elements for list2:")
for i in range(a):
    n = int(input())
    list2.append(n)
r = []
i = 0
j = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        r.append(list1[i])
        i += 1
    else:
        r.append(list2[j])
        j += 1
while i < len(list1):
    r.append(list1[i])
    i += 1

while j < len(list2):
    r.append(list2[j])
    j += 1
print("Merged list:", r)