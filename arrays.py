#Arrays work with data of the same type while list can carry data of different tyrpes

courses = ["MIT", "DatatScience", "Cybersecurity"]

#Accessing an element in an array
print(courses[1])

#Looping through an array
for course in courses:
    print("Course is ", course)

#Method to add new element to array
courses.append("Android Development")
print(courses)

#Method to delete an element in an array 
courses.remove("MIT")
print(courses)