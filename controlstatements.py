temperature = int(input("Enter temperature:"))

if temperature > 25:
    print("It's hot outside")
    
else:
    print("It is too cold")

# Python program that checks three numbers and returns the smallest 

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if num1 < num2 and num1 < num3 : 
    print(num1, "is the smallest number")

elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")

else:
    print(num3, "is the smallest number")

#Return the largest number

num4 = 22
num5 = 33
num6 = 44

if num4 > num5 and num4 > num6:
    print(num4, "is the largest number")

elif num5 > num4 and num5 > num6:
    print(num5, "is the largest number")

else:
    print(num6, "is the largest number")