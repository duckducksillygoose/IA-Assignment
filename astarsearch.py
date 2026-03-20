#use the astar algorithm for pathfinding


from IAGraph import *
from LinkedListsetup import *


def find_lowest_f(open_set):
    lowest = open_set[0]

    for object in open_set:
        if object.f <=lowest.f:
            lowest = object

        return lowest


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
    open_set = [start_city]
    closed_set = []


    print(start_node.g)
    print(start_node.h)

    #explore neighbour sets, aka one with a road relationship
    #pick neighbour city with the smallest h
    #move to open set
    #repeat until u reach target city, then reverse path
    

