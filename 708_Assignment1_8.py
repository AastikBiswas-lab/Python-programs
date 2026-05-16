x = int(input("Enter the first length of the triangle:"))
y = int(input("Enter the second length of the triangle:"))
z = int(input("Enter the third length of the triangle:"))
if x + y > z and y + z > x and z + x > y:
    print("Valid Triangle")
    if x==y==z:
        print("Equilateral Triangle")
    elif x==y or y==z or z==x:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid Triangle")