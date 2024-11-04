#Built in - functions that already exist in python library that you can work with

#max function
y = max(34, 56, 70 , 18)
print(y) # Output: 70

#min function
x = min(40, 67, 34, 25)
print(x) # Output: 25

#POW function
x = pow(2, 3)
print(x) # Output: 8

#User-defined functions - User to define(gives it name and what it should do )
def greeting():
    print("Hello there!")

greeting() # Output: Hello there!

def multiply():
    a = 5
    b = 10
    print(a * b) # Output: 35

multiply()

#Parameteres(Variable) & Arguments(Value that you get to store in a variable)

def add(x, y):
    print(x + y) # Output: 9

add(4,5)
add(90,5)

def employee(fName, age, position,status):
    print(fName,age,position,status)

employee("Faith Wanjiru", 23, "HR", "single")
employee("Mart Wambu", 33, "CEO", "married")
employee("Grace Lunar", 53, "Receprionist", "married")