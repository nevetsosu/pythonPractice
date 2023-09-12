from node import node

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