class student:
    #Properties/attributes/variables/characteristics
    name = "Evans"
    gender = "male"
    age = 32
    #Methods/functions/actions/behaviours
    def study(self):
        print("student is studying")

#First object
student1 = student() #This is creating an object(Instatiation)
student1.study()
print(student1.name)

#Second object
student2 = student()
student2.study()