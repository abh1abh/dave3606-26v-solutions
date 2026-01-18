from sys import argv


def read_graph(filename):
    # Reads file
    with open(filename) as f:
        content = f.read()

    # Parse the content
    lines = content.splitlines()
    print(lines[0])

    # First line: number of nodes and edges
    num_nodes, num_edges = map(int, lines[0].split())
    print(f"Number of nodes: {num_nodes}, number of edges: {num_edges}")

    # Get node values
    node_values = [int(lines[i + 1]) for i in range(num_nodes)]

    # Get edges
    edges = [[] for _ in range(num_nodes)]
    for line in lines[1 + num_nodes :]:
        parts = line.split()

        if len(parts) != 2:
            # This catches the "start node" line (like "2")
            continue
        from_node, to_node = map(int, parts)
        edges[from_node].append(to_node)
    return node_values, edges


def dfs(node, edges, node_values, visited):
    # Depth-first search to sum node values
    # If already visited, return 0
    if node in visited:
        return 0
    # Mark as visited
    visited.add(node)
    # Start total with this node's value
    total = node_values[node]
    # Recurse for each neighbor
    for neighbor in edges[node]:
        total += dfs(neighbor, edges, node_values, visited)
    return total


def main():
    if len(argv) != 2:
        print("Remember to provide filename")
        return

    filename = argv[1]

    node_values, edges = read_graph(filename)
    print(node_values)
    print(edges)

    visited = set()
    total_value = dfs(0, edges, node_values, visited)
    print(f"Nodes visited from node 0: {visited}")
    print(f"Total value of nodes visited from node 0: {total_value}")


if __name__ == "__main__":
    main()
