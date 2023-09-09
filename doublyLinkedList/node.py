class Node:
    def __init__(self, data : any = 0, left_node : 'Node' = None, right_node : 'Node' = None) -> None:
        if (left_node != None): self.left_node = left_node
        if (right_node != None): self.right_node = right_node
        self.data = data