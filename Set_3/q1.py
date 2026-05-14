# 1. Write a python program to display a user entered name followed by Good Afternoon using input() function.

# name = input("Enter your name: ")
# print("Good Afternoon,", name)

# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

# name = input("Enter your name: ")
# date = input("Enter date: ")

# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)

# print(letter)

# 3. Write a program to detect double space in a string.

# str="How are  you!"
# print(str.find("  "))  

# 4. Replace the double space from problem 3 with single spaces.

# print(str.find(" "))

# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)

