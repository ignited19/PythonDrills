class Node:

    def __init__(self, data):
        self.children = []
        self.data = data
        self.visited = False

    def display_tree(self, root):
        for children in root:
            print(children.data)

    def bfs(self, root):
        stack = []
        stack.append(root)

        while len(stack) != 0:
            current_node = stack.pop(0)
            print(f"value:{current_node.data}, {type(current_node)}, {current_node.visited}")

            for child in current_node.children:
                print(f"add children: {child.data} {type(child)}")

                if child.visited == False:
                    stack.append(child)

                current_node.visited = True
