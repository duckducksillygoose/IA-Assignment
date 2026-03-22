from LinkedListsetup import *
from cities import *

#hill climbing algorithm

def hill_climb(graph, start_node, end_node):
        
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
        print("Nodes found") #copied over code from a star search
