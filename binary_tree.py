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
    
    def simetric_traversal(self,node='ROOT'):
        #inorder travessal
        
        if node == 'ROOT':
            node = self.root
            
        if node.left:
            self.simetric_traversal(node.left)
        
        print(node)

        if node.right:
            self.simetric_traversal(node.right)   
    
    def simetric_traversal_arr(self,node='ROOT',arr=[]):
      #inorder travessal returning an array 
      
      if node == 'ROOT':
        node = self.root 
        arr =[]
 
      if node.left:
          self.simetric_traversal_arr(node.left,arr)
        
      arr.append(node.data)

      if node.right:
        self.simetric_traversal_arr(node.right,arr) 
        
        return arr     
    
    def postorder_traversal(self,node='ROOT'):
        
        if node == 'ROOT':
            node = self.root
            
        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)      
        
        print(node)

    def height(self,node= 'ROOT'):
        
        if node == 'ROOT':
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

    def levelorder_traversal(self,node='ROOT'):
        
        if node == 'ROOT':
            node = self.root

        queue=[]
        queue.append(node)

        while len(queue):

            node = queue[0]
            queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(node)


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

    def _search(self, value, node = 'ROOT'):

        if node == 'ROOT':
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    
    def min(self,node = 'ROOT'):

        if node == 'ROOT':
            node = self.root
        
        while node.left:
            node = node.left
        return node.data

    def max(self,node = 'ROOT'):

        if node == 'ROOT':
            node = self.root
        
        while node.right:
            node = node.right
        return node.data      

    def remove(self,value,node='ROOT'):
        
        if node == 'ROOT':
            node = self.root
        
        if node is None:
            return node
            
        if value < node.data:
            node.left = self.remove(value,node.left)
        
        elif value > node.data:
            node.right = self.remove(value,node.right)

        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data  = substitute
                node.right = self.remove(substitute,node.right)
        return node
                 

if __name__ == "__main__":

    tree = BinarySearchTree()

    # --- For loop insert

    values = [10,8,63,2,9,60,82]

    for i in values:
        tree.insert(i)


    print(tree.simetric_traversal_arr())

    print('\n--------')
    tree.remove(10)

    print(tree.simetric_traversal_arr() )
    print('\n--------')
    tree.levelorder_traversal()
        


    #   ---- Hard insert 

    #    N1=Node(10)
    #    N2=Node(8)
    #    N3=Node(63)
    #    N4=Node(2)
    #    N5=Node(9)
    #    N6=Node(60)
    #    N7=Node(82)

    #    N1.right = N3
    #    N1.left  = N2
    #    N2.right = N5
    #    N2.left  = N4
    #    N3.right = N7
    #    N3.left  = N6
    #    tree.root= N1

    #    print('simetric_traversal')
    #    tree.simetric_traversal()
    #    print(tree.root)
    #    print('postorder_traversal')
    #    print(tree.max())