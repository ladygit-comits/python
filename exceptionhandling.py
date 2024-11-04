
try:
    number = 3
    print(number)


except:
    print("An error has occured")

num1 = 45
num2 = 5
try:
    print(num1/num2)
except:
    print("Error: Division by zero is not allowed")
finally:
    print("Success")