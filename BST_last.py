class node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if not root:
            return node(data)
        
        if data > root.data:
            root.right = self._insert(root.right, data)

        if data < root.data:
            root.left = self._insert(root.left, data)

        return root
    
    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self,root):
        if root:
            self._inorder(root.left)
            print(root.data,end=' ')
            self._inorder(root.right)

    def successor(self, root):
        while root and root.right:
            root = root.right
        return root

    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return None
        elif root.data < key:
            root.right = self._delete(root.right, key)
        elif root.data > key:
            root.left = self._delete(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                new_node = self.successor(root.left)
                self._delete(self.succesor(root.left).data)
                return new_node
                
            

if __name__ == '__main__':
    tree = BST()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(60)
    tree.inorder()