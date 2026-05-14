# 1. Store seven fruits entered by the user

fruits = []

for i in range(7):
    fruit = input("Enter fruit name: ")
    fruits.append(fruit)

print("Fruits List:", fruits)

# 2. Accept marks of 6 students and display them in sorted manner

marks = []

for i in range(6):
    mark = int(input("Enter marks: "))
    marks.append(mark)

marks.sort()

print("Sorted Marks:", marks)


# 3. Check that tuple type cannot be changed in python

a = (1, 2, 3)

# a[0] = 5   # This will give an error because tuple is immutable

print("Tuple:", a)


# 4. Sum a list with 4 numbers

numbers = [10, 20, 30, 40]

print("Sum of list:", sum(numbers))

# 5. Count number of zeros in tuple

a = (7, 0, 8, 0, 0, 9)

print("Number of zeros:", a.count(0))