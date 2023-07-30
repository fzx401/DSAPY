from pydantic import BaseModel
from typing import Any

class Node(BaseModel):
    data : Any
    next : "Node" = None

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def convert_nums_to_linklist(self, nums: list):
        """将数组转化为单向链表

        Args:
            nums (list): 待转化数组

        """
        if not nums:
            raise ValueError("数组为空")
        nums = nums[::-1]
        self.head = Node(data=nums.pop())
        cur = self.head
        while nums:  # 表面上操作的是cur，实际上是Node
            tmp = Node(data=nums.pop())
            cur.next = tmp
            cur = tmp
        # return self.head
    
    @property
    def is_empty(self):
        """链表是否为空

        Returns:
            bool: True or False
        """
        return self.head is None

    def add_head(self, data) -> None:
        """链表头部插入数据

        Args:
            data (_type_): 待插入数据
        """
        if self.is_empty:
            new_node = Node(data=data)
            self.head = new_node
        else:
            new_node = Node(data=data)
            new_node.next = self.head  # 先将当前data的next指针指向已有链表的头节点
            self.head = new_node  # 然后将head指针指向新链表整体

    def add_tail(self, data) -> None:
        """链表尾部插入数据

        Args:
            data (_type_): 待插入数据
        """
        if self.is_empty:
            new_node = Node(data=data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data=data)
            self.tail.next = new_node
            self.tail = new_node

    @property
    def length(self) -> int:
        """链表长度

        Returns:
            int: 整数长度
        """
        if self.is_empty:
            return 0
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index)->"Node.data":
        """取下标位置的数据

        Args:
            index (_type_): 下标

        Returns:
            Node.data: 节点数据
        """
        if self.is_empty:
            return "链表为空"
        elif self.length_of_link_list() - 1 < index:
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
        elif pos >= self.length:
            self.add_tail(val)
        else:
            new_node = Node(data=val)
            idx = 0
            cur = self.head
            while idx < pos - 1:
                idx += 1
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node       

    def reverseList(self)-> Node:
        if self.is_empty:
            raise ValueError('链表为空')
        cur = self.head
        pre = None
        
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
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
        else:
            while cur.next:
                if cur.next.data == val:
                    tmp = cur.next.next
                    cur.next = tmp
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
        return '——>'.join(str(i) for i in res)