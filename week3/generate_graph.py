from random import randint, shuffle
from sys import argv

num_nodes = int(argv[1])
num_edges = int(argv[2])
if num_edges < num_nodes - 1:
    raise Exception("Too few edges")
print(num_nodes, num_edges)

# Generate the number that is to be stored in each node.
# The underscore is an ordinary variable, but it's customary
# in Python to use it to indicate that we don't care about the value
# of the loop variable (we need to perform `num_nodes` iterations,
# but we don't need to know which iteration we're currently in).
for _ in range(num_nodes):
    print(randint(1, 99))

# Ensure that there exists at least one (long) path through all the
# nodes, so that every node will be reachable from the start node.
guaranteed_route = list(range(num_nodes))
shuffle(guaranteed_route)
print(guaranteed_route[0])  # Start node
for i in range(len(guaranteed_route) - 1):
    from_node = guaranteed_route[i]
    to_node = guaranteed_route[i + 1]
    print(from_node, to_node)

# Then, generate the rest of the edges completely randomly
# (this might result in some pairs of nodes having multiple edges
# between each other in the same direction, and some nodes having
# self-loops, but that's fine).
for _ in range(num_edges - num_nodes + 1):
    from_node = randint(0, num_nodes - 1)
    to_node = randint(0, num_nodes - 1)
    print(from_node, to_node)
