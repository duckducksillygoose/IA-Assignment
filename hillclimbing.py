from LinkedListsetup import *
from IAGraph import *
from cities import *

#hill climbing algorithm

def hillclimb(graph, start_city, goal_city):
        
    # Find cairns and perth
    current = graph.nodelist.head
    start_node = goal_node = None
    while current:
        if current.data.name == start_city:
            start_node = current.data
        if current.data.name == goal_city: #copied over code from a star search
            goal_node = current.data
        current = current.next

    if start_node is None or goal_node is None:
        raise Exception("Start or goal node not found!")
    else:
        print("Nodes found") 

    path = []

    current_node = start_node


    while True:
        path.append(current_node.name)

        if current_node.name == goal_node.name:
            print("Goal city has been reached")
            print("Final Path:", " -> ".join(path))


        
        best_neighbour = None
        best_h = current_node.h

        neighbour_current = current_node.neighbours.head

        while neighbour_current:
            neighbour = neighbour_current.data.n #GraphEdge object


            if neighbour.h < best_h:
                best_h = neighbour.h #replace with new best
                best_neighbour = neighbour #label as best

            neighbour_current = neighbour_current.next #update

        if best_neighbour == None:
            print("Reached local optimum, cannot go any further")
            print("Final Path:", " -> ".join(path))
            return path #reaches the local optimum
        

        current_node = best_neighbour


