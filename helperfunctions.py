from IAGraph import *
from cities import *
from LinkedListsetup import *


#functions that help the search functions

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
    path.reverse()

    return path

def total_cost(goal_node):
    cost = 0
    current = goal_node
    while current.parent:
        prev = current.parent

        neighbour_node = prev.neighbours.head
        while neighbour_node:
            edge = neighbour_node.data
            if edge.n == current:
                cost += edge.weight
                break
            neighbour_node = neighbour_node.next

        current = prev
    print("The total cost of this journey is", cost)
    return cost
