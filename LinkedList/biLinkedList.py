from pydantic import BaseModel
from typing import Any

class Node(BaseModel):
    data : Any
    next : "Node" = None
    prev : "Node" = None

class BiDLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def convert_nums_to_linklist(self, nums: list) -> None:
        """将数组转化为双向链表

        Args:
            nums (list): 待转化数组

        """
        if not nums:
            raise ValueError("数组为空")
        nums = nums[::-1]
        self.head = Node(data=nums.pop())
        cur = self.head
        while nums:  
            tmp = Node(data=nums.pop())
            cur.next = tmp
            tmp.prev = cur
            cur = tmp
        self.tail = cur
            
    @property
    def is_empty(self) -> bool:
        """链表是否为空

        Returns:
            bool: True or False
        """
        return not self.head
    
    def add_head(self, val: int) -> None:
        """链表头部插入数据

        Args:
            data (_type_): 待插入数据
        """
        new_node = Node(data=val)
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def add_tail(self, val: int) -> None:
        """链表尾部插入数据

        Args:
            data (_type_): 待插入数据
        """
        new_node = Node(data=val)
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    @property
    def length(self)-> int:
        """链表长度

        Returns:
            int: 整数长度
        """
        if self.is_empty:
            return 0
        cur, cnt = self.head, 1
        while cur.next:
            cur = cur.next
            cnt += 1
        return cnt
    
    def __getitem__(self, index)->"Node.data":
        """取下标位置的数据

        Args:
            index (_type_): 下标

        Returns:
            Node.data: 节点数据
        """
        if self.is_empty():
            return "链表为空"
        elif self.length - 1 < index:
            return "索引值溢出"
        else:
            count, current = 0, self.head
            while current.next and count < index:
                count += 1
                current = current.next
            return current.data
            
    def insert(self, pos, val)->None:
        """在某位置插入

        Args:
            pos (_type_): 从0开始的位置
            val (_type_): 插入节点的数值

        Returns:
            _type_: None
        """
        if pos <= 0:
            self.add_head(val)
        elif pos >= self.length - 1:
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
            cur.next.prev = new_node
            cur.next = new_node
    
    # def travel(self)->list:
    #     if not self.head:
    #         return []
    #     cur = self.head
    #     res = []
    #     while cur:
    #         res.append(cur.data)
    #         cur = cur.next
    #     return res
    
    def pop(self)->'Node.data':
        tail_node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        
        return tail_node.data
    
    def popleft(self)->'Node.data':
        head_node = self.head
        self.head = self.head.next
        self.head.prev = None
        
        return head_node.data
    
    def remove(self, val):
        """移除链表中某个节点

        Args:
            val (_type_): 节点数值

        Return: None
        """
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
            while cur.next:
                if cur.next.data == val:
                    tmp = cur.next.next
                    cur.next = tmp
                    if tmp:
                        tmp.prev = cur
                    return
                else:
                    cur = cur.next
            raise ValueError("There is no val in the linkedlist")
        
    def __str__(self) -> str:
        res = []
        if self.is_empty:
            return "链表为空"
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        return '<——>'.join(str(i) for i in res)
        
    
            
        
        
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