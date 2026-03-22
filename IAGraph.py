from LinkedListsetup import LinkedList, ListNode

import numpy as np


class IAGraph():
    def __init__(self, size):
        self.size = size
        self.nodelist = LinkedList()

    
    def add_node(self, name, h):
        node = GraphNode(name,h )
        self.nodelist.InsertNode(node)


    def add_road(self, city1, city2, weight):
        node1 = node2= None #have to initialise to get rid of datatype as None has no datatype

        node1 = node2 = None

        current = self.nodelist.head

        while current:
            if current.data.name == city1:
                node1 = current.data

            if current.data.name == city2:
                node2 = current.data

            current = current.next

        if node2 is None or node1 is None:
            raise Exception("Nodes not found")

        node1.neighbours.InsertNode(GraphEdge(node2, weight)) #bidirectional
        node2.neighbours.InsertNode(GraphEdge(node1, weight))

    def display_as_list(self):
        current = self.nodelist.head
        while current:
            node = current.data

            neighbours_array = np.empty(10, dtype=object)
            count = 0

            neighbour_current = node.neighbours.head
            while neighbour_current and count < len(neighbours_array):
                edge = neighbour_current.data     # GraphEdge object
                neighbours_array[count] = (edge.n.name, edge.weight)
                count += 1
                neighbour_current = neighbour_current.next

            space_used = neighbours_array[:count]

            print(node.name, "<->" ,space_used)
            current = current.next

        print("All towns listed")



 

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








