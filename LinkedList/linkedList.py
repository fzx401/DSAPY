
__all__ = ['Node', 'LinkList']

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self, nums: list):
        self.head = self._convert_nums_to_linklist(nums)

    def _convert_nums_to_linklist(self, nums: list):
        if not nums:
            raise ValueError("数组为空")
        nums = nums[::-1]
        head = Node(nums.pop())
        cur = head
        while nums:  # 表面上操作的是cur，实际上是Node
            tmp = Node(nums.pop())
            cur.next = tmp
            cur = tmp
        return head

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head  # 先将当前data的next指针指向已有链表的头节点
            self.head = new_node  # 然后将head指针指向新链表整体

    def insert_at_end(self, data):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def length_of_link_list(self):
        if self.is_empty():
            return 0
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        if self.is_empty():
            return "链表为空"
        elif self.length_of_link_list() - 1 < index:
            return "索引值溢出"
        else:
            count, current = 0, self.head
            while current.next and count < index:
                count += 1
                current = current.next
            return current.data

    def insert_at_index(self, data, index):
        if self.is_empty():
            return "链表为空"
        elif index == 0:
            return self.insert_at_beginning(data)
        elif index == self.length_of_link_list() - 1:
            return self.insert_at_end(data)
        else:
            new_node = Node(data)
            pre = self[index - 1]
            new_node.next = pre.next
            pre.next = new_node

