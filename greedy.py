

from LinkedListsetup import *
from cities import *
from IAGraph import *
from astarsearch import reconstruct_path

#notes for doing this algorithm
#find the start and end nodes
# find neighbours and calculate the heuristic, compare all neighbours and find the lowest heuristic
#choose that neighbour and repeat
#different to hill climbing that f=h, also uses manhattan distance so have to code that



def greedy_BFS(graph, start_city, goal_city): #copied from astar
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


    current = graph.nodelist.head
    open_set = [start_node]
    closed_set=[]
    exploration=[]

    start_node.parent = None



    while open_set:
            # find node with smallest h manually
        lowest_index = 0
        i = 1
        while i < len(open_set):
            if open_set[i].h < open_set[lowest_index].h:
                lowest_index = i
            i += 1

        current = open_set.pop(lowest_index)
        print("Expanding:", current.name, "| h =", current.h) #gets the node with the lowest index
        exploration.append(current) #becomes part of the path

        if current == goal_node:
                path = reconstruct_path(goal_node)
                print("Final path", " -> ".join(path))
                return
            
        closed_set.append(current)

        neighbour_node = current.neighbours.head
        while neighbour_node:
            neighbour = neighbour_node.data.n
            if neighbour not in closed_set:
                if neighbour not in open_set:
                    open_set.append(neighbour)
                    neighbour.parent = current

            neighbour_node = neighbour_node.next #iterate




    