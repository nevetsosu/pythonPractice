from LinkedList import LinkedList

def main(): 
    testList = LinkedList("test")
    testList.enforceType(False)
    testList.append_node(0)
    testList.append_node("APP")
    testList.append_node(123)

    testList.enforceType(True, bool)

    print(testList.data_type)
    print(type(testList.start_node.data))

    for i,d in enumerate(LinkedList.iterateBy(testList, 10)):
        print(i, d)

    for i,d in enumerate(LinkedList.iterateBy(testList, 10)):
        print(i, type(d))

if __name__ == "__main__" : main()