a = int(input("Enter the size of the dictionary: "))
dict1 = {}
for i in range(a):
    k = input("Enter the key: ")
    v = input("Enter the value: ")
    dict1[k] = v
print("The dictionary is: ", dict1)
for key,values in dict1.items():
    print("The key is: ", k)
    print("The value is: ", v)