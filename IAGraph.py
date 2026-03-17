from LinkedListsetup import LinkedList, ListNode




class IAGraph():
    def __init__(self, size):
        self.size = size
        self.nodelist = LinkedList()

class GraphNode():
    def __init__(self, name, h):
        self.name = name
        self.neighbours = LinkedList()
        self.h = h #heuristic cost from cell to target
        self.g = float("inf") #cost from start to this cell
        self.f = float("inf") #total


    def add_node(self, name):
        node = GraphNode(name)
        self.nodelist.InsertNode(node)


class GraphEdge():
    def __init__(self, n, weight):
        self.n= n
        self.weight = weight





