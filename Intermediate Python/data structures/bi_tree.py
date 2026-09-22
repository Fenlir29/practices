class Node:

  def __init__(self, data, left=None ,right=None):
    self.data = data
    self.left = left
    self.right = right

class Binary_tree:

    def __init__(self):
        self.root = None

    def print_bi_tree(self, new_node):

        if new_node is not None:
            self.print_bi_tree(new_node.left)
            print(new_node.data)
            self.print_bi_tree(new_node.right)