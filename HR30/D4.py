"""
Objective
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, 
it's only enabled in certain languages. Check out the Tutorial tab for learning materials and an instructional video!
"""
class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.age = 0
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge


    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age < 13:
            print("You are young.")
        elif 13 <= age < 18:
            print("You are a teenager.")
        elif age >= 18:
            print("You are old.")

    def yearPasses(self):    
        # Increment the age of the person in here
        global age #Variable para tomar la variable global de age y modificarla
        age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")