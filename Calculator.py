def sum(a , b):
    return  a + b 

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b
    

str1 = "Welcome to the Calculator"
print(str1.center(100))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input(''' Enter your Given Operation to perform :
          "1" for sum 
          "2" for subtract
          "3" for multiply
          "4" for divide 
          Enter Your Selected Operation : '''))
if c == 1:
    result1 = sum(a,b)
    print("The Sum of two numbers is: ", result1)
elif c == 2:
    result2 = subtract(a,b)
    print("The Subtraction of two numbers is: ", result2)
elif c == 3:
    result3 = multiply(a,b)
    print("The Multiplication of two numbers is: ", result3)
elif c == 4:
    result4 = divide(a,b)
    print("The Division of two numbers is: ", result4)
else:
    print("Invalid Operation Selected")
