import os
import json
class LinkedList:
    def __init__(self, start_data : any, enforce_type : bool = True):
        self.size = 1
        self.enforce_type = enforce_type
        self.data_type = type(start_data)
        self.start_node = node(start_data)
        self.start_node.left_node = self.start_node
        self.start_node.right_node = self.start_node

    def iterateBy(self, count : int) -> list:
        itr = self.start_node
        dir : bool
        values = list()
        
        if (count > 0): dir = True
        elif (count < 0): dir = False
        else: return list

        for i in range(0, count):
            values.append(itr.data)
            if (dir): itr = itr.right_node
            else: itr = itr.left_node

        return values
    
    def enforceType(self, enforce : bool, data_type : type = None):
        if (data_type != None): self.data_type = data_type

        self.enforce_type = enforce

        self.__enforce_types()

    def __enforce_types(self):
        itr = self.start_node

        for i in range(0, self.size):
            itr.data = self.data_type(itr.data)
            itr = itr.right_node
    
    def append_node(self, data):
        refined_data : any

        if (self.enforce_type): refined_data = self.data_type(data)
        else: refined_data = data

        end_node = self.start_node.right_node

        new_node = node(refined_data, left_node = self.start_node, right_node = end_node)
        self.start_node.right_node = new_node

        self.size += 1 


class node:
    def __init__(self, data : any, left_node : 'node' = None, right_node : 'node' = None):
        self.left_node : 'node' = left_node
        self.right_node : 'node' = right_node

        self.data : any = data


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