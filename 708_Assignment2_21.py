a = int(input("Enter the size of the list: "))
list1 = []
print("Enter the elements of the list: ")
for i in range(a):
    b = int(input())
    list1.append(b)
target = int(input("Enter the target value: "))
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] + list1[j] == target:
            print("The  two numbers that add up to the target are: ", list1[i], "and", list1[j])