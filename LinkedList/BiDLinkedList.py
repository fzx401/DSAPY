from pydantic import BaseModel

class Node(BaseModel):
    data : int
    next : "Node" = None
    prev : "Node" = None

class BiDLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        
    @property
    def is_empty(self) -> bool:
        return not self.head
    
    def add_head(self, val: int) -> None:
        new_node = Node(data=val)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def add_tail(self, val: int) -> None:
        new_node = Node(data=val)
        if self.is_empty:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    @property
    def length(self)-> int:
        if self.is_empty:
            return 0
        cur, cnt = self.head, 1
        while cur.next:
            cur = cur.next
            cnt += 1
        return cnt
            
    def insert(self, pos, val):
        if pos <= 0:
            self.add_head(val)
        elif pos >= self.length:
            self.add_tail(val)
        else:
            new_node = Node(data=val)
            idx = 0
            cur = self.head
            while idx < pos - 1:
                idx += 1
                cur = cur.next
            new_node.prev = cur
            new_node.next = cur.next
            cur.next = new_node
            cur.next.prev = new_node
    
    def travel(self)->list:
        if not self.head:
            return []
        cur = self.head
        res = []
        while cur:
            res.append(cur.data)
            cur = cur.next
        return res
    
    def remove(self, val):
        if self.is_empty:
            raise ValueError("LinkedList is empty")
        cur = self.head
        if cur.data == val:
            if self.length==1:
                self.head = None
            else:
                self.head = cur.next
                cur.next.prev = None
        else:
            while cur:
                if cur.data == val:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    return
                else:
                    cur = cur.next
            raise ValueError("There is no val in the linkedlist")
            
        
    
            
        
        
if __name__ == "__main__":
    linked_list = BiDLinkedList()
    head_node = Node(data=1)
    linked_list.head = head_node
    linked_list.add_tail(2)
    linked_list.add_tail(3)
    linked_list.add_tail(4)
    print(linked_list.travel())
    linked_list.insert(2,val=5)
    print(linked_list.travel())
    linked_list.remove(3)
    print(linked_list.travel())