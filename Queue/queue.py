import sys
import os

sys.path.append(os.path.abspath('.'))
from LinkedList.linkedList import LinkList, Node
from typing import Any

class Queue(LinkList):
    def __init__(self):
        super().__init__()
    
    def enqueue(self, val: Any)->None:
        self.add_tail(val)
        
    def dequeue(self)->None:
        if self.is_empty:
            raise ValueError("队列为空")
        tmp = self.head
        self.remove(self.head.data)
        return tmp
    
    def peek(self)->"Node":
        return self.head.data

if __name__ == "__main__":
    q = Queue()
    q.enqueue(3)
    q.enqueue(2)
    pass