from IAGraph import *
from LinkedListsetup import *
from astarsearch import *
from hillclimbing import *

testgraph = IAGraph(8)
#Initialising nodes
testgraph.add_node("Perth", 3400)
testgraph.add_node("Adelaide", 2200)
testgraph.add_node("Melbourne", 2300)
testgraph.add_node("Canberra", 2100)
testgraph.add_node("Sydney", 1950)
testgraph.add_node("Newcastle", 1850)
testgraph.add_node("Brisbane", 1400)
testgraph.add_node("Gold Coast", 1500)
testgraph.add_node("Hobart", 2600)
testgraph.add_node("Darwin", 1700)
testgraph.add_node("Alice Springs", 1500)
testgraph.add_node("Townsville", 280)
testgraph.add_node("Cairns", 0)



#adding relationships
testgraph.add_road("Perth", "Adelaide", 2700)
testgraph.add_road("Perth", "Darwin", 4000)
testgraph.add_road("Adelaide", "Melbourne", 730)
testgraph.add_road("Adelaide", "Alice Springs", 1530)
testgraph.add_road("Alice Springs", "Darwin", 1500)
testgraph.add_road("Adelaide", "Darwin", 3000)
testgraph.add_road("Melbourne", "Canberra", 660)
testgraph.add_road("Melbourne", "Hobart", 1100)

testgraph.add_road("Canberra", "Sydney", 300)
testgraph.add_road("Canberra", "Newcastle", 180)
testgraph.add_road("Sydney", "Newcastle", 160)
testgraph.add_road("Sydney", "Brisbane", 920)
testgraph.add_road("Newcastle", "Brisbane", 780)
testgraph.add_road("Brisbane", "Gold Coast", 80)
testgraph.add_road("Brisbane", "Townsville", 1350)
testgraph.add_road("Townsville", "Cairns", 350)

testgraph.display_as_list()
hill_climb(testgraph, "Perth", "Cairns")