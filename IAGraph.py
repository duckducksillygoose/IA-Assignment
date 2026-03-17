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
        city1 = city2 = None #have to initialise to get rid of datatype as None has no datatype

        current = self.nodelist.headN #searches through nodelist
        while current:
            if current.data.data == city1:
                city1 = current.data
            if current.data.data == city1:
                
                city2 = current.data
            current = current.next

        if city1 is None or city2 is None:
            raise Exception("One or both nodes not found") #check against misspellings
        


        city1.neighbours.InsertNode(GraphEdge(city2, weight)) #bidirectional
        city2.neighbours.InsertNode(GraphEdge(city1, weight))

    def display_as_list(self):
        current = self.nodelist.head
        while current:
            node = current.data

            neighbours_array = np.empty(10, dtype=object)
            count = 0

            neighbour_current = node.neighbours.head
            while neighbour_current and count < len(neighbours_array):
                edge = neighbour_current.data     # GraphEdge object
                neighbours_array[count] = (edge.n.data, edge.weight)
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


testgraph = IAGraph(8)
testgraph.add_node("Perth", 3400)
testgraph.add_node("Adelaide", 2200)
testgraph.add_node("Melbourne", 2300)
testgraph.add_node("canberra", 2100)
testgraph.add_node("sydney", 1950)
testgraph.add_node("Newcastle", 1850)
testgraph.add_node("Brisbane", 1400)
testgraph.add_node("Gold Coast", 1500)
testgraph.add_node("Hobart", 2600)
testgraph.add_node("Darwin", 1700)
testgraph.add_node("Alice Springs", 1500)
testgraph.add_node("Townsville", 280)
testgraph.add_node("Cairns", 0)
testgraph.display_as_list()





