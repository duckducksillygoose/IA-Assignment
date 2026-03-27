from hillclimbing import *
from cities import *
from astarsearch import *
from greedy import *
from helperfunctions import *

import time

nx_graph =testgraph.convert_to_nx()
print(type(nx_graph))



nx.draw(nx_graph, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', edge_color='blue')
plt.show()
#plt.show()

#testgraph.display_as_list()

#time.sleep(2)
#print("Printing hill climb")
#time.sleep(2)
#print("____HILL CLIMB RESULTS______")
#hillclimb(testgraph, "Perth", "Cairns")
#time.sleep(2)


#print("____GREEDY BEST FIRST SEARCH RESULTS______")
#greedy_BFS(testgraph, "Perth", "Cairns")



#notes to go from next coding session.
# print final path for a star search rather than just node expansion
#work on greedy
#print trees for everything