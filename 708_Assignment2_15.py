
s = input("Enter a sentence: ")
w = s.split()
count = {}
list1 = []
list2 = []
for i in w:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
    list1.append(i)
    list2.append(count[i])
dict1 ={}
dict1 = dict(zip(list1, list2))
print(dict1)