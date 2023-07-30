from Queue.deque import Deque
from LinkedList.linkedList import LinkList
from LinkedList.biLinkedList import BiDLinkedList

class foo:
    pass

if __name__ == "__main__":
    
    l = BiDLinkedList()
    l.convert_nums_to_linklist([1, 2, 3, 4, 5])
    print(l)
    l.remove(2)
    print(l)