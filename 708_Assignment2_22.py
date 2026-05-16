s = input("Enter a string: ")
list1 = []
list2 = []
count = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        list1.append(s[i:j])
for i in range(len(list1)):
    y = list1[i]
    count = 0
    for j in range(len(y)):
        for k in range(j+1, len(y)):
            if y[j] == y[k]:
                count = count + 1
    if count == 0:
        list2.append(y)
list4 = []
for i in range(len(list2)):
    c= len(list2[i])
    list4.append(c)
max1 = max(list4)
for i in range(len(list2)):
    if len(list2[i]) == max1:
        print("The longest substring with no repeated characters is:", list2[i])