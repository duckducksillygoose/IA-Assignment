from LinkedListsetup import LinkedList, ListNode

class IAGraph():
    def __init__(self, size):
        self.size = size

class GraphNode():
    def __init__(self, name, h):
        self.name = name
        self.neighbours = LinkedList()
        self.h = h #heuristic cost from cell to target
        self.g = float("inf") #cost from start to this cell
        self.f = float("inf") #total


class GraphEdge():
    def __init__(self, n, weight):
        self.n= n
        self.weight = weight
