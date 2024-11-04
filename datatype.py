number = 56 #Integer
second = 43.12 #Float
text = "Greeting" #String
isPythonIntresting = True #Boolean

#Data Structure- Multiple values stored in a single variable.
cars = ["toyota","nissan", "vw"]#This is a list- Ordered and changeable
fruits = ("banana","orange","apple") #Tuple - elements are ordered but unchangeable

print(number + second, isPythonIntresting)

countries = {"Kenya", "Tunisia", "Algeria"} #This is a set -  Elements do not follow any order and are unchangeable


student = {
    "name": "John",
    "age": 20,
    "city": "Nairobi"
    } #This is a dictionary key value pair - elements are ordered and changeable
print(cars)
print(fruits)
print(countries)
print(student)
print(student["age"])

#Determining a datatype 
print(type(student))
print(type(countries))

#typecasting - converting one datatype to another
print(int(second))
print(float(number))