

from LinkedListsetup import *
from cities import *
from IAGraph import *
from astarsearch import reconstruct_path

#notes for doing this algorithm
#find the start and end nodes
# find neighbours and calculate the heuristic, compare all neighbours and find the lowest heuristic
#choose that neighbour and repeat
#different to hill climbing that f=h, also uses manhattan distance so have to code that



def greedy_BFS(graph, start_city, end_city): #copied from astar
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
    path=[]

    visited = []

    while open_set:
            # find node with smallest h manually
        lowest_index = 0
        i = 1
        while i < len(open_set):
            if open_set[i].h < open_set[lowest_index].h:
                lowest_index = i
            i += 1

            current = open_set.pop(lowest_index) #gets the node with the lowest index
            closed_set.append(current) #visited

            if current == goal_node:
                print("Goal found")
                return 



    