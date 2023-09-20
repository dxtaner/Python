class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


# Kök düğümü oluşturalım
root = TreeNode("A")

# Ağacın yapısını oluşturalım
root.children.append(TreeNode("B"))
root.children.append(TreeNode("C"))

root.children[0].children.append(TreeNode("D"))
root.children[0].children.append(TreeNode("E"))

root.children[1].children.append(TreeNode("F"))
root.children[1].children.append(TreeNode("G"))
