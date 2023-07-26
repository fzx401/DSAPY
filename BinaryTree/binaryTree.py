from pydantic import BaseModel
from typing import Any


__all__ = ['BinaryTree']

class BinaryTree(BaseModel):
    val : Any = None
    leftChild : "BinaryTree" = None
    rightChild : "BinaryTree" = None

    def insertLeft(self, val)-> None:
        if not self.leftChild:
            self.leftChild = BinaryTree(val=val)
            return
        return self.leftChild.insertLeft(val)

            
    def insertRight(self, val)-> None:
        if not self.rightChild:
            self.rightChild = BinaryTree(val=val)
            return
        return self.rightChild.insertLeft(val)

    def isLeaf(self)-> bool:
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self)-> 'BinaryTree':
        return self.rightChild

    def getLeftChild(self)-> 'BinaryTree':
        return self.leftChild

    def setRootVal(self,val)-> None:
        self.val = val

    def getRootVal(self,)-> None:
        return self.val

    def inorder_traversal(self)-> list:
        if not self:
            raise ValueError("No tree found!")
        res = []

        def recur(root):
            if not root:
                return
            recur(root.leftChild)
            res.append(root.val)
            recur(root.rightChild)
        recur(self)
        return res

    def postorder_traversal(self)-> list:
        if not self:
            raise ValueError("No tree found!")
        res = []

        def recur(root):
            if not root:
                return
            recur(root.leftChild)
            recur(root.rightChild)
            res.append(root.val)
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
            recur(root.leftChild)
            recur(root.rightChild)
        recur(self)
        return res
    
    @property       
    def height(self):
        if not self:
            return 0
        left_height = self.leftChild.height if self.leftChild else 0
        right_height = self.rightChild.height if self.rightChild else 0

        return 1 + max(left_height, right_height)
    
    @property
    def length(self)-> int:
        return len(self.inorder_traversal())

if __name__ == "__main__":
    tree = BinaryTree(val=1)
    tree.insertLeft(val=2)
    pass