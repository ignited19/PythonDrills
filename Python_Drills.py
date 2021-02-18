import StringOperations as SO
import Node as Node


print("Let's rock")
#=========================================================
# Python Drills - Strings
#=========================================================

#SO.StringOperations.UniqueCharCheck()
SO.StringOperations.CheckStringDiff()

#=========================================================
# Python Drills - Strings
#=========================================================

#Nodes to create a tree
root = Node.Node("root")
a = Node.Node("a")
b = Node.Node("b")
c = Node.Node("c")
d = Node.Node("d")
e = Node.Node("e")
f = Node.Node("f")

#Create edges towards the nodes
root.children = [a, b, c, d]
a.children.append(e)
a.children.append(f)


#Check to verify what is in the graph
#root.display_tree(root.children)

root.bfs(root)
