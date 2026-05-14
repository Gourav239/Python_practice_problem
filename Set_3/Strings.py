# Strings are immutable in python

name="Rohit"
state="Uttar Pradesh"
n=len(name) # len -> length of string

print(name[2])
print(name[-2]) # negative indexing is also in python
print(state[1:3]) # [1,3)

print(name[:4]) # [0,4)
print(name[0:]) # [0,n) , where n=len(name)

print(state[1:7:2]) # string from index 1 to 6 and 2nd char from current index

print(name)
print(n)

str = "harry"
capitalized = str.capitalize()
print(capitalized) # Output: Harry

str = "harry"
capitalized = str.capitalize()
print(capitalized) # Output: Harry

str = "harry"
print(str.endswith("rry")) # Output: True

str = "harry"
index = str.find("rr")
print(index) # Output: 2

str = "harry"
replaced = str.replace("r", "l")
print(replaced) # Output: hally