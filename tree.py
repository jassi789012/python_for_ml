class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self):
        spaces = '      ' * self.getLevel()
        print(spaces +"|-"+self.data)
        if self.children:
            for child in self.children:
                child.printTree()
    

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Surface"))
    laptop.addChild(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.addChild(TreeNode("iphone"))
    cellphone.addChild(TreeNode("Google Pixel"))
    cellphone.addChild(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("Samsung"))
    tv.addChild(TreeNode("LG"))

    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.printTree()
    # print(root.children[0].getLevel())