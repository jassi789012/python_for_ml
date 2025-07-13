class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BST(data)
        
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BST(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)

            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)

            else:
                return False
            
    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()
    
    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()

    def delete(self,val):
        pass
        

def build_tree(elements):
    root = BST(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root


if __name__ == "__main__":

    numbers = [17 ,4 ,1 ,20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))