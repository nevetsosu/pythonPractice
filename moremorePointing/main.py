class Node:
    def __init__(self, id) -> None:
        self.next_node : Node
        self.id = id
    
def main() -> None:
    lis = [Node(0), Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)]

    # connect everything together going to the right        
    for i,d in enumerate(lis[0:-1]):
        d.next_node = lis[i + 1]
        d.id = i
    lis[-1].next_node = lis[0]

    iterator = lis[0]

    for i in range(0, len(lis)):
        print(iterator.id)
        iterator = iterator.next_node

    print("----")
    print("current main iterator pos: ", iterator.id)

    iterateWithNewVariable(lis, lis[3], 2)

    print("current main iterator pos: ", iterator.id)

    iterate(lis, lis[1], 2)

    print("current main iterator pos: ", iterator.id)

    for i in lis:
        print(i.id)



def iterateWithNewVariable(lis : list, start_node : Node, amount : int):

    if (amount < 0): amount *= -1
    amount %= len(lis)   

    iterator = start_node

    for i in range(0, amount):
        print(iterator.id)
        iterator = iterator.next_node

def iterate(lis : list, start_node : Node, amount : int):

    # try to modify the original data first before changing the assignment of the variable
    start_node.id = 1000

    if (amount < 0): amount *= -1
    amount %= len(lis)

    for i in range(0, amount):
        print(start_node.id)
        start_node = start_node.next_node
        

if __name__ == "__main__": main()