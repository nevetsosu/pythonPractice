class node:
    def __init__(self, data : any, left_node : 'node' = None, right_node : 'node' = None):
        self.left_node : 'node' = left_node
        self.right_node : 'node' = right_node

        self.data : any = data
