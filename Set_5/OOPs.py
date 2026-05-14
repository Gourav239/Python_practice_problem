# class Student:
#     school="RKMEC"
    
#     def __init__(self, roll, name):
#         self.roll = roll
#         self.name = name
    
# s1=Student(22,"ABC")
# s2=Student(23,"XYZ")
# print(s1.school)    
# print(s1.name)    
# print(s2.name) 

# Inheritance

# Parent class
# class Animal:

#     def speak(self):
#         print("Animal makes a sound")


# # Child class inheriting Animal
# class Dog(Animal):

#     def bark(self):
#         print("Dog barks")


# # object of child class
# d1 = Dog()

# d1.speak()   # inherited from Animal
# d1.bark()    # method of Dog  
 

class BankAccount:

    # constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # deposit money
    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited")

    # withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn")
        else:
            print("Insufficient balance")

    # display account details
    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


# creating objects
a1 = BankAccount("Gourav", 5000)
a2 = BankAccount("Rahul", 3000)

# operations
a1.deposit(2000)
a1.withdraw(1000)
a1.display()

print()

a2.withdraw(4000)
a2.display()