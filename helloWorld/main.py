mystr = "this is a string"

newlist = [1,2,3,4,5,6]

print(newlist[0:len(newlist)])

def someFunction():
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)

def anotherFunction():
    global mystr
    mystr = "def2"
    print(mystr)

anotherFunction()
print(mystr)

del mystr
print(mystr)

print("hello world")