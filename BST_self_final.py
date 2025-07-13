class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current_node, data):
        
        if data < current_node.data:
            
            if current_node.left is None:
                current_node.left = node(data)
            else:
                self._insert(current_node.left, data)

        elif data > current_node.data:
            
            if current_node.right is None: 
                current_node.right = node(data)
            else:
                self._insert(current_node.right, data)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

if __name__ == '__main__':
    tree1 = BST()
    tree1.insert(10)
    tree1.insert(20)
    tree1.insert(30)
    tree1.insert(40)
    tree1.inorder()