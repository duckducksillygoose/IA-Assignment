from LinkedListsetup import LinkedList, ListNode




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
testgraph.add_node("2", 400)
testgraph.add_node("4", 420)
testgraph.add_node("3", 462)
testgraph.add_node("1", 826)
testgraph.add_node("8", 321)
testgraph.add_node("9", 847)
print(testgraph.nodelist)




