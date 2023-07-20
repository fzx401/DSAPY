from typing import Union, List
from pydantic import BaseModel, StrictInt, StrictFloat

__all__ = ['BinarySearchTree']
class BinarySearchTree(BaseModel):

    val: Union[StrictInt, StrictFloat, None] = None
    left: "BinarySearchTree" = None
    right: 'BinarySearchTree' = None

    def insert(self, value: Union[int, float]) -> None:
        if self.val:
            if value < self.val:
                if self.left is None:
                    self.left = BinarySearchTree(val=value)
                else:
                    self.left.insert(value)
            elif value > self.val:
                if self.right is None:
                    self.right = BinarySearchTree(val=value)
                else:
                    self.right.insert(value)
        else:
            self.val = value

    def find(self, data: Union[int, float])-> bool:
        if data < self.val:
            if not self.left:
                return False
            return self.left.find(data)
        elif data > self.val:
            if not self.right:
                return False
            return self.right.find(data)
        else:
            return True
    @staticmethod
    def trans_list_to_bst(arr: List) -> "BinarySearchTree":
        root = BinarySearchTree(val=arr[0])
        for i in range(1, len(arr)):
            root.insert(arr[i])
        
        return root

    def delete(self, value)-> "BinarySearchTree":
        if self is None:
            raise ValueError('No tree found!')
        # if value == self.val:
        #     raise ValueError('Please use deleteroot() instead!')
        if value < self.val:  # 当要删除的节点小于当前节点，递归向左下寻找并删除
            self.left = self.left.delete(value)
        elif value > self.val:  # 当要删除的节点大于当前节点，递归向右下寻找并删除
            self.right = self.right.delete(value)
        else:  # 当找到要删除的节点
            if self.is_leaf():  # 当该节点为叶子节点时，直接返回空
                return None
            elif not self.left:  # 当该节点有右孩子没有左孩子时,直接返回右孩子
                # tmp = self.right
                # self = None
                return self.right
            elif not self.right:  # 当该节点有左孩子没有右孩子时,直接返回左孩子
                # temp = self.left
                # self = None
                return self.left
            # 当该节点有左右孩子时，将其右子树中的最小值赋给当前节点，并在其右子树中递归删除该值
            temp = self.right.minimum()
            self.val = temp.val
            self.right = self.right.delete(temp.val)
        return self

    def minimum(self)->"BinarySearchTree":
        #  直到找到没有左子树的节点为止，直接返回
        if not self.left:
            return self
        return self.left.minimum()

    def maximum(self)->"BinarySearchTree":
        if not self.right:
            return self
        return self.right.maximum()

    def inorder_traversal(self)-> list:
        if not self:
            raise ValueError("No tree found!")
        res = []

        def recur(root):
            if not root:
                return
            #  先对左子树递归遍历
            recur(root.left)
            res.append(root.val)
            #  再对右子树递归遍历
            recur(root.right)

        recur(self)
        return res

    def preorder_traversal(self)-> list:
        if not self:
            raise ValueError("No tree found!")
        res = []

        def recur(root):
            if not root:
                return
            res.append(root.val)
            #  先对左子树递归遍历
            recur(root.left)
            #  再对右子树递归遍历
            recur(root.right)

        recur(self)
        return res

    def postorder_traversal(self)-> list:
        if not self:
            raise ValueError("No tree found!")
        res = []

        def recur(root):
            if not root:
                return
            #  先对左子树递归遍历
            recur(root.left)
            #  再对右子树递归遍历
            recur(root.right)
            res.append(root.val)

        recur(self)
        return res

    @property
    def length(self)-> int:
        return len(self.inorder_traversal())

    @property
    def height(self)-> int:
        if not self:
            return 0

        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        return max(left_height, right_height) + 1

    @property
    def is_bst(self)-> bool:
        if self.left:
            if self.left.val > self.val or not self.left.is_bst:
                return False

        if self.right:
            if self.right.val < self.val or not self.right.is_bst:
                return False

        return True
    
    @property
    def is_leaf(self)-> bool:
        return not self.left and not self.right
    
if __name__ == '__main__':
    nums = [20,1,5,2,3,6]
    tree = BinarySearchTree.trans_list_to_bst(nums)
    tree = tree.delete(20)

