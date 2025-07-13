import tkinter as tk
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        if key > root.val:
            root.right = self._insert(root.right, key)
        return root
    
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.val,end=' ')
            self._inorder(root.right)

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, root, val):
        found = False
        if root.val == val:
            found = True
            return found
        if val < root.val:
            self._search(root.left, val)
        if val > root.val:
            self._search(root.right, val)
        return found

    def print_tree(self):
        def _get_lines(node):
            if node is None:
                return [], 0, 0, 0  # lines, width, height, root_index

            line1 = []
            line2 = []

            node_str = str(node.val)
            new_root_width = len(node_str)

            # Get left and right subtrees
            l_lines, l_width, l_height, l_root = _get_lines(node.left)
            r_lines, r_width, r_height, r_root = _get_lines(node.right)

            # First line: root with left and right branches
            if l_width > 0:
                l_root_pos = l_root + 1
                line1.append(' ' * l_root_pos + '_' * (l_width - l_root_pos))
                line2.append(' ' * l_root + '/')
            else:
                line1.append('')
                line2.append('')

            line1[0] += node_str

            if r_width > 0:
                line1[0] += '_' * r_root
                line2[0] += ' ' * new_root_width + '\\' + ' ' * (r_root - 1)
            else:
                line2[0] += ''

            # Merge lines
            new_lines = [line1[0], line2[0]]

            # Combine left and right lines
            for i in range(max(l_height, r_height)):
                left_line = l_lines[i] if i < l_height else ' ' * l_width
                right_line = r_lines[i] if i < r_height else ' ' * r_width
                new_lines.append(left_line + ' ' * new_root_width + right_line)

            return new_lines, l_width + new_root_width + r_width, max(l_height, r_height) + 2, l_width + new_root_width // 2

        lines, *_ = _get_lines(self.root)
        for line in lines:
            print(line)


    def draw1(self):
        # Create Tkinter window
        window = tk.Tk()
        window.title("Binary Search Tree Visualization")
        canvas = tk.Canvas(window, width=800, height=600, bg="white")
        canvas.pack()

        def draw_node(node, x, y, dx, depth):
            if node is None:
                return

            radius = 20
            # Draw node (circle)
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="skyblue")
            canvas.create_text(x, y, text=str(node.val), font=("Arial", 12, "bold"))

            # Draw left subtree
            if node.left:
                canvas.create_line(x, y + radius, x - dx, y + 60 - radius)
                draw_node(node.left, x - dx, y + 60, dx // 2, depth + 1)

            # Draw right subtree
            if node.right:
                canvas.create_line(x, y + radius, x + dx, y + 60 - radius)
                draw_node(node.right, x + dx, y + 60, dx // 2, depth + 1)

        draw_node(self.root, 400, 50, 160, 0)

        window.mainloop()


    def draw2(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.axis('off')

        def assign_positions(node, depth=0, pos_dict={}, x=0):
            if node is None:
                return x
            x = assign_positions(node.left, depth + 1, pos_dict, x)
            pos_dict[node] = (x, -depth)
            x += 1
            x = assign_positions(node.right, depth + 1, pos_dict, x)
            return x

        def draw_edges(node, pos_dict):
            if node.left:
                x0, y0 = pos_dict[node]
                x1, y1 = pos_dict[node.left]
                ax.plot([x0, x1], [y0, y1], 'k-')
                draw_edges(node.left, pos_dict)
            if node.right:
                x0, y0 = pos_dict[node]
                x1, y1 = pos_dict[node.right]
                ax.plot([x0, x1], [y0, y1], 'k-')
                draw_edges(node.right, pos_dict)

        def draw_nodes(pos_dict):
            for node, (x, y) in pos_dict.items():
                circle = plt.Circle((x, y), 0.3, color='skyblue', ec='black')
                ax.add_patch(circle)
                ax.text(x, y, str(node.val), fontsize=12, ha='center', va='center')

        pos_dict = {}
        assign_positions(self.root, 0, pos_dict)
        draw_edges(self.root, pos_dict)
        draw_nodes(pos_dict)
        ax.set_xlim(-1, max([x for x, _ in pos_dict.values()]) + 1)
        ax.set_ylim(min([y for _, y in pos_dict.values()]) - 1, 1)
        plt.show()



    
if __name__ == '__main__':
    Tree1 = BST()
    Tree1.insert(50)
    Tree1.insert(50)
    Tree1.insert(30)
    Tree1.insert(20)
    Tree1.insert(40)
    Tree1.insert(70)
    Tree1.insert(60)
    Tree1.insert(80)
    Tree1.inorder()
    Tree1.print_tree()
    # Tree1.draw1()
    # Tree1.draw2()
    print(Tree1.search(80))