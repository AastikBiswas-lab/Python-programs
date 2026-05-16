def binary_search(arr, l, h, k):
    if l > h:
        return -1   
    mid = (l + h) // 2
    if arr[mid] == k:
        return mid
    elif k < arr[mid]:
        return binary_search(arr, l, mid - 1, k)
    else:
        return binary_search(arr, mid + 1, h, k)
a = int(input("Enter number of elements: "))
list1 = []
print("Enter the elements:")
for i in range(a):
    a = int(input())
    list1.append(a)
list1.sort(reverse=False)
k = int(input("Enter number to search: "))
result = binary_search(list1, 0, len(list1) - 1, k)
if result != -1:
    print("Element found at index:", result+1)
else:
    print("Element not found")
