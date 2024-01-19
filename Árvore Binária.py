class BSTNode (object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


root = BSTNode(4)
root.left = BSTNode(1)
root.right = BSTNode(9)
root.left.left = BSTNode(2)
