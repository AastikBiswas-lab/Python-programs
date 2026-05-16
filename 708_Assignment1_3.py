print("enter 1 for area of circle")
print("enter 2 for area of rectangle")
print("enter 3 for area of triangle")
print("enter 4 for area of square")
print("enter 5 for area of parallelogram")
print("enter 6 for volume of cube")
print("enter 7 for volume of cuboid")
print("enter 8 for volume of sphere")
print("enter 9 for volume of cylinder")
print("enter 10 for volume of cone")
ch = int(input("enter your choice: "))
match ch:
    case 1:
        r = int(input("enter radius: "))
        area = 3.14 * r * r
        print("area of circle is: ", area)
    case 2:
        l = int(input("enter length: "))
        b = int(input("enter breadth: "))
        area = l * b
        print("area of rectangle is: ", area)
    case 3:
        b = int(input("enter base: "))
        h = int(input("enter height: "))
        area = (1* b * h)/2
        print("area of triangle is: ", area)
    case 4:
        s = int(input("enter side: "))
        area = s * s
        print("area of square is: ", area)
    case 5:
        b = int(input("enter base: "))
        h = int(input("enter height: "))
        area = b * h
        print("area of parallelogram is: ", area)
    case 6:
        s = int(input("enter side: "))
        vol = s * s * s
        print("volume of cube is: ", vol)
    case 7:
        l = int(input("enter length: "))
        b = int(input("enter breadth: "))
        h = int(input("enter height: "))
        vol = l * b * h
        print("volume of cuboid is: ", vol)
    case 8:
        r = int(input("enter radius: "))
        vol = (4 * 3.14 * r * r * r)/3
        print("volume of sphere is: ", vol)
    case 9:
        r = int(input("enter radius: "))
        h = int(input("enter height: "))
        vol = 3.14 * r * r * h
        print("volume of cylinder is: ", vol)
    case 10:
        r = int(input("enter radius: "))
        h = int(input("enter height: "))
        vol = (1 * 3.14 * r * r * h)/3
        print("volume of cone is: ", vol)
