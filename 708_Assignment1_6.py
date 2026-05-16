
def power_set(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        temp = i   
        for j in range(n):
            if temp % 2 == 1:
                subset.append(arr[j])
            temp = temp // 2   
        print(subset)

a = int(input("Enter the size of list: "))
list1 = []
print("Enter the elements of the list: ")
for i in range(a):
    b= int(input())
    list1.append(b)
power_set(list1)