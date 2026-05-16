def addition(a, b):
    sum = a+b
    return sum
def subtraction(a, b):
    difference = a-b
    return difference
def multiplication(a, b):
    product = a*b
    return product
def division(a, b):
     if(b==0):
            return " Division by zero not possible"
     else :
            div = a/b
            return div
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("The sum of the two numbers is: ", addition(x, y))
print("The difference of the two numbers is: ", subtraction(x, y))
print("The product of the two numbers is: ", multiplication(x, y))
print("The division of the two numbers is: ", division(x, y))