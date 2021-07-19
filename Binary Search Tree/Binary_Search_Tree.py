import sys
sys.path.append("..")
from Node.Tree_Node import Tree_Node

class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self,item):
        current = self.root
        if self.root == None: # BST is empty
            node = Tree_Node()
            node.data = item
            self.root = node

        else:
            while current != None:
                if item > current.data:
                    if current.rchild != None:
                        current = current.rchild
                    else:
                        node = Tree_Node()
                        node.data = item
                        current.rchild = node
                        break
                else:
                    if current.lchild != None:
                        current = current.lchild
                    else:
                        node = Tree_Node()
                        node.data = item
                        current.lchild = node
                        break

    def traversal_inorder(self):
        print("Inorder: ",end="")
        self.inorder(self.root)
        print()

    def inorder(self,root_pointer):
        if root_pointer != None:
            self.inorder(root_pointer.lchild)
            print(root_pointer.data,end=" ")
            self.inorder(root_pointer.rchild)

    def traversal_preorder(self):
        print("Preorder: ",end="")
        self.preorder(self.root)
        print()

    def preorder(self,root_pointer):
        if root_pointer != None:
            print(root_pointer.data, end=" ")
            self.preorder(root_pointer.lchild)
            self.preorder(root_pointer.rchild)

    def traversal_postorder(self):
        print("Postorder: ",end="")
        self.postorder(self.root)
        print()

    def postorder(self,root_pointer):
        if root_pointer != None:
            self.postorder(root_pointer.lchild)
            self.postorder(root_pointer.rchild)
            print(root_pointer.data,end=" ")

    def get_height(self):
        h = self.height(self.root)
        #print(f"Height : {h}")
        return h

    def height(self,root_pointer):
        if root_pointer.lchild == None and  root_pointer.rchild == None:
            return 1
        else:
            if self.height(root_pointer.lchild) >self.height(root_pointer.rchild):
                return self.height(root_pointer.lchild) + 1
            else:
                return self.height(root_pointer.rchild) + 1

if __name__ == "__main__":
    BST = Binary_Tree()
    BST.insert(2)
    BST.insert(3)
    BST.insert(1)
    BST.traversal_inorder()
    BST.traversal_preorder()
    BST.traversal_postorder()
    BST.get_height()



