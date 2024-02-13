class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return
    print(node.data, end='')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end='')
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='')

if __name__ == "__main__":
    N = int(input())
    tree = {}

    for _ in range(N):
        root, left, right = input().split()
        if root not in tree:
            tree[root] = Node(root)
        if left != '.':
            tree[left] = tree.get(left, Node(left))
            tree[root].left = tree[left]
        if right != '.':
            tree[right] = tree.get(right, Node(right))
            tree[root].right = tree[right]

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
