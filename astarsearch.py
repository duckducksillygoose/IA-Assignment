#use the astar algorithm for pathfinding


from IAGraph import *
from LinkedListsetup import *
from helperfunctions import *




def astar(graph, start_city, goal_city):

    
    # Find cairns and perth
    current = graph.nodelist.head
    start_node = goal_node = None
    while current:
        if current.data.name == start_city:
            start_node = current.data
        if current.data.name == goal_city:
            goal_node = current.data
        current = current.next

    if start_node is None or goal_node is None:
        raise Exception("Start or goal node not found!")
    else:
        print("Nodes found")

    start_node.g = 0
    start_node.f = start_node.h
    open_set = [start_node]
    closed_set = []

    while open_set:
        current_node = find_lowest_f(open_set)
        print("Expanding", current_node.name, "f=",current_node.f, "g=", current_node.g, "h=", current_node.h)


        if current_node == goal_node:
            path= reconstruct_path(goal_node)
            cost = total_cost(goal_node)

                
            print("Final path:", " -> ".join(path))
            return path 

        open_set.remove(current_node)
        closed_set.append(current_node)

        neighbour_node = current_node.neighbours.head

        while neighbour_node:
            edge = neighbour_node.data
            neighbour = edge.n
            cost = edge.weight

            if neighbour in closed_set:
                neighbour_node = neighbour_node.next
                continue

            possible_g = current_node.g + cost

            if neighbour not in open_set:
                open_set.append(neighbour)
            elif possible_g >= neighbour.g:
                neighbour_node = neighbour_node.next
                continue

            neighbour.parent = current_node
            neighbour.g = possible_g
            neighbour.f = neighbour.g + neighbour.h

            neighbour_node = neighbour_node.next
                


            