from node import Node

class LinkedList:  
    def __init__(self) -> None:

        self.start_node : Node = Node()  
        self.end_node : Node = Node()
        self.current_node : Node = self.start_node
        self.num_nodes = 2

        # connect the beginning and end together
        self.end_node.right_node = self.start_node
        self.end_node.left_node = self.start_node

        self.start_node.left_node = self.end_node
        self.start_node.right_node = self.end_node

    # moves current node to the right
    def move_right(self, moves : int = 1) -> None:
        for i in range(0, moves):
            self.current_node = self.current_node.right_node
    
    # moves current node to the left
    def move_left(self, moves : int = 1) -> None:
        for i in range(0, moves):
            self.current_node = self.current_node.left_node

    # returns the data of the current node
    def data(self) -> any:
        return self.current_node.data
    
    def set(self, data) -> None:
        self.current_node.data = data

    # if the number of nodes to add is negative, they will be added to the left of the current node. default_data for all the instanciated nodes can also be optionally specified.
    def add_nodes(self, num_nodes : int = 0, default_data : any = None) -> None:
        if (num_nodes > 0):
            self.__add_nodes_right(num_nodes, default_data)
        elif (num_nodes < 0):
            self.__add_nodes_left(num_nodes, default_data)
    
    def __add_nodes_right(self, num_nodes : int = 0, default_data : any = None) -> None:
        current_node = self.current_node
        end_node = current_node.right_node

        self.num_nodes = self.num_nodes + num_nodes

        for i in range(0, num_nodes):
            new_node = Node(default_data, left_node = current_node)
            current_node.right_node = new_node

            current_node = current_node.right_node

        end_node.left_node = current_node
        current_node.right_node = end_node

    def __add_nodes_left(self, num_nodes : int = 0, default_data : any = None) -> None:
        current_node = self.current_node
        end_node = current_node.left_node

        index = num_nodes * -1
        self.num_nodes = self.num_nodes + num_nodes
        
        for i in range(0, index):
            new_node = Node(default_data, right_node = current_node)
            current_node.left_node = new_node

            current_node = current_node.left_node

        end_node.right_node = current_node
        current_node.left_node = end_node
        
    # left iterator generator
    def IterateLeft(self, step : int = 1) -> None:
        current_node = self.current_node

        if (step < 0): step * -1
        for i in range(0, step):
            yield current_node.data
            current_node = current_node.left_node

    # right iterator generator                                  # find a way to make these functions more modular maybe make them into a different class
    def IterateRight(self, step : int = 1) -> None:
        current_node = self.current_node

        if (step < 0): step * -1
        for i in range(0, step):
            yield current_node.data
            current_node = current_node.right_node

    
class IterateRight:
    def __init__(self, list : LinkedList, step : int = 1) -> None:
        self.current_node = list.current_node.left_node
        self.index = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0: raise StopIteration

        self.index = self.index - 1
        self.current_node = self.current_node.right_node

        return self.current_node.data