class KdTreeNode(object):
    def __init__(self, x, y):
        self.left  = None
        self.right = None
        self.cord = (x, y)

class KdTree(object):
    def __init__(self, nodes):
        self.nodes = nodes

    def find_median(self, nodes, axis):

    def build_tree(self, nodes, axis):
        if not nodes:
            return

