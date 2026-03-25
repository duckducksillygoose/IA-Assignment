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

