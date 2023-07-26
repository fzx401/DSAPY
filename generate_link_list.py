"""
Step1：构建头节点，将cur指向当前节点
Step2：令cur.next指向数组中下一个数构造的Node
Step3：令cur指向cur.next
"""


class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def generate_link_list(nums: list):
    nums = nums[::-1]
    head = LinkNode(nums.pop())
    cur = head
    while nums:
        tmp = LinkNode(nums.pop())
        cur.next = tmp
        cur = tmp
    return head


nums = [1, 2, 3, 4, 5]
h = generate_link_list(nums)
pass
