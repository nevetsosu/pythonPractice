value = input("Enter something: ").lower()

match value:
    case "your mom":
        print(1)
    case "your dad":
        print(2)
    case "your granny":
        print(3)


lis = [0,1,2,3,4,5]
for x in lis:
    print(x)

print("---")  

for x in lis:
    print(x * 2)

print("---")

for i in lis:
    if (i % 2 == 0): continue
    print(i * 3)

# for i, j in {"test": 1, "test2": 2}:
#     print(i, d)

print("---")

for i, j in enumerate(enumerate(enumerate(lis))):
    print(i, j)
