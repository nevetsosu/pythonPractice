import copy
from main import Node

lis = [Node(0), Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)]
newlist : list

def displayStats(list1 : list, list2 : list, size : int):
    if (size > len(list1) or size > len(list2)):
        print("warning: specified size is bigger than the smallest list, defaulting to the smallest list size")

    print("SAME LIST ASSIGNMENT?", list1 is list2)

    for i in range(0, size):
        print("Values: {val1:2d} {val2:2d} IDs: {id1:s} {id2:s} SAME? {same:s}".format(val1 = list1[i].id, val2 = list2[i].id, id1 = str(list1[i]), id2 = str(list2[i]), same = str(list1[i] is list2[i])))

def main():
    # assignment 
    print("ASSIGNMENT")
    newlis = lis

    lis.append(Node(11))
    newlis.append(Node(22))

    displayStats(lis, newlis, len(lis))
    print("---")

    # shallow copy
    print("SHALLOW COPY")
    newlis = lis[:]

    lis.append(Node(33))
    newlis.append(Node(44))

    displayStats(lis, newlis, len(lis))
    print("---")

    # another shallow copy using copy
    print("SHALLOW COPY USING COPY")
    newlis = copy.copy(lis)

    lis.append(Node(55))
    newlis.append(Node(66))

    displayStats(lis, newlis, len(lis))
    print("---")
    
    # deep copy
    print("DEEP COPY")
    newlis = copy.deepcopy(lis)

    lis.append(Node(77))
    newlis.append(Node(88))

    displayStats(lis, newlis, len(lis))
    print("---")

# connect everything together going to the right        
for i,d in enumerate(lis[0:-1]):
    d.next_node = lis[i + 1]
    d.id = i
lis[-1].next_node = lis[0]

main()