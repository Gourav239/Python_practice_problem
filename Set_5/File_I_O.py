'''
Modes Of Opening A File : -

r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode.
'''

f=open("dummy.txt","r")
content=f.read()
print(content)
f.close()

f=open("dummy.txt","w")
msg="Good morning !"
f.write(msg)
print("Update succesful")
f.close()

