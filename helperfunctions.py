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



def get_edge_cost(graph, start_city, end_city):
    current = graph.nodelist.head

    while current:
        if current.data.name == start_city:
            neighbour_node = current.data.neighbours.head

            while neighbour_node:
                if neighbour_node.data.n == end_city:
                    return neighbour_node.data.weight  # use your cost field

                neighbour_node = neighbour_node.next

        current = current.next


