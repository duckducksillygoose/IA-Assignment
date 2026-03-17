from IAGraph import *
from LinkedListsetup import *

testgraph = IAGraph(8)
testgraph.add_node("Perth", 3400)
testgraph.add_node("Adelaide", 2200)
testgraph.add_node("Melbourne", 2300)
testgraph.add_node("canberra", 2100)
testgraph.add_node("sydney", 1950)
testgraph.add_node("Newcastle", 1850)
testgraph.add_node("Brisbane", 1400)
testgraph.add_node("Gold Coast", 1500)
testgraph.add_node("Hobart", 2600)
testgraph.add_node("Darwin", 1700)
testgraph.add_node("Alice Springs", 1500)
testgraph.add_node("Townsville", 280)
testgraph.add_node("Cairns", 0)

testgraph.display_as_list()