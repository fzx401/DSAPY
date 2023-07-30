import sys
import os

sys.path.append(os.path.abspath('.'))
from LinkedList.biLinkedList import BiDLinkedList, Node
from typing import Any

class Deque(BiDLinkedList):
    def __init__(self) -> None:
        super().__init__()
        # self.deque = BiDLinkedList()
        
    def append(self, val : Any) -> None:
        self.add_tail(val)
        # self.deque.add_tail(val)
        
    def appendleft(self, val : Any) -> None:
        self.add_head(val)
        # self.deque.add_head(val)
    
    def pop(self) -> "Node":
        if self.is_empty:
            raise ValueError("队列为空")
        return self.pop()
    
    def popleft(self) -> "Node":
        if self.is_empty:
            raise ValueError("队列为空")
        return self.popleft()
    
    def peek(self) -> "Node":
        return self.head.data
    
    
if __name__ == "__main__":
    q = Deque()
    q.append(3)
    q.append(4)
    q.append(5)
    peek = q.peek()
    print(peek)