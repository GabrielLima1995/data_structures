#!/bin/python3
#Para fins de aprendizado esse codigo foi adaptado de PythonCafe   
#https://github.com/python-cafe/data_structures/blob/master/arvores/tree.py
#This is a binary tree algorithm 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    
    def simetric_traversal(self,node=None):
        #inorder travessal
        
        if node is None:
            node = self.root
            
        if node.left:
            self.simetric_traversal(node.left)
        
        print(node)

        if node.right:
            self.simetric_traversal(node.right)        
    
    def postorder_traversal(self,node=None):
        
        if node is None:
            node = self.root
            
        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)      
        
        print(node)

    def height(self,node=None):
        
        if node is None:
            node = self.root

        hleft  = 0
        hright = 0 
            
        if node.left:
            hleft = self.height(node.left)

        if node.right:
            hright = self.height(node.right)          
        
        if hright > hleft :
            return hright + 1
        else:
            return hleft + 1

class BinarySearchTree(BinaryTree):

    def insert(self,value):
        parent=None
        x = self.root
        while(x):
            parent=x
            if value < x.data:
                x = x.left
            else:
                x = x.right
            
        if parent is None:
            self.root =   Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right= Node(value)
    

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)



            



if __name__ == "__main__":

   tree = BinarySearchTree()
   N1=Node(10)
   N2=Node(8)
   N3=Node(63)
   N4=Node(2)
   N5=Node(9)
   N6=Node(60)
   N7=Node(82)

   N1.right = N3
   N1.left  = N2
   N2.right = N5
   N2.left  = N4
   N3.right = N7
   N3.left  = N6
   tree.root= N1

   #print('simetric_traversal')
   #tree.simetric_traversal()
   #print(tree.root)
   #print('postorder_traversal')
   tree.simetric_traversal()


