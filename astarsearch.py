#use the astar algorithm for pathfinding


from IAGraph import *
from LinkedListsetup import *


def find_lowest_f(open_set): #should take node objects
    lowest = open_set[0]

    for object in open_set:
        if object.f <=lowest.f:
            lowest = object

        return lowest
    


def reconstruct_path(goal_node):
    path = []
    current = goal_node

    while current:
        path.append(current.name)
        current = current.parent

    return list(reversed(path))




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

    while open_set: #while there are nodes
        current_node = find_lowest_f(open_set)
        print(current_node.f)

        if current_node == goal_node:
            return reconstruct_path
        
        open_set.remove(current_node)
        closed_set.append(current_node)

        for neighbour, cost in current_node.neighbours:
            if neighbour in closed_set:
                continue #if the neighbour has not so far been explored

            possible_g = current_node.g + cost

            if neighbour not in open_set:
                open_set.append(neighbour)#add the neighbour to the set to be considered

            elif possible_g >=neighbour.g:
                continue

            neighbour.g = possible_g
            neighbour.f = neighbour.g + neighbour.h



            