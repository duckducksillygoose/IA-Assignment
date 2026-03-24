from hillclimbing import *
from cities import *
from astarsearch import *
from greedy import *

import time

testgraph.display_as_list()

#time.sleep(2)
#print("Printing hill climb")
#time.sleep(2)

#hillclimb(testgraph, "Perth", "Cairns")
#time.sleep(2)

#print("Doing astar")
##astar(testgraph, "Perth", "Cairns")

print("Doing gbfs")
greedy_BFS(testgraph, "Perth", "Cairns")



#notes to go from next coding session.
# print final path for a star search rather than just node expansion
#work on greedy
#print trees for everything