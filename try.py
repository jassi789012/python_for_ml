class node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.no_of_nodes = 0

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        
        if not root:
            self.no_of_nodes += 1
            return node(data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        elif data < root.data:
            root.left = self._insert(root.left, data)
        
        return root
    
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.data, end=' ')
            self._inorder(root.right)


    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, root):
        if root:
            print(root.data, end=' ')
            self._preorder(root.left)
            self._preorder(root.right)


    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, root): 
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.data, end=' ')

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root:
            return False
        elif key > root.data:
            return self._search(root.right, key)
        elif key < root.data:
            return self._search(root.left, key)
        else:
            return True
        
    def succesor(self, root):
        root = root.right
        while root and root.left:
            root = root.left
        return root
        
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        
        if not root:
            return None
        elif key > root.data:
            root.right = self._delete(root.right, key)
        elif key < root.data:
            root.left = self._delete(root.left, key)
        else:

            self.no_of_nodes -= 1 

            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                succ = self.succesor(root)
                root.data = succ.data
                root.right = self._delete(root.right, succ.data)



if __name__ == '__main__':
    
    tree1 = BST()
    tree1.insert(10)
    tree1.insert(20)
    tree1.insert(30)
    tree1.insert(40)
    tree1.insert(50)
    tree1.insert(60)
    tree1.inorder()
    print(" ")
    # print(tree1.search(30))
    # print(tree1.search(300))
    print(tree1.no_of_nodes)