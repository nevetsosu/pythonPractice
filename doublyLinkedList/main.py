from LinkedList import LinkedList, IterateRight

LL1 = LinkedList()

for i in range (1, 10):
    LL1.add_nodes(1, i)
    LL1.move_right()

LL1.move_right(2)

iter = LinkedList.IterateRight(LL1, 40)

for i in iter:
    print(i)