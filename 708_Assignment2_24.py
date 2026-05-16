a = int(input("Enter the size of the list: "))
list1 = []
print()
for i in range(a):
    num = int(input())
    list1.append(num)
k = int(input("Enter the value of k: "))
count = {}
for i in list1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
freq_list = list(count.items())
freq_list.sort(key=lambda x: x[1], reverse=True)
print("Top", k, "frequent elements:")
for i in range(k):
    print(freq_list[i][0])