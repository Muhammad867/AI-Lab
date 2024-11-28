graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def dls(node, goal, depth, visited):  # Depth-Limited Search
    if depth == 0:
        return False
    if node not in visited:
        print(node)
        visited.add(node)
        if node == goal:
            return True
        for neighbour in graph[node]:
            if dls(neighbour, goal, depth - 1, visited):
                return True
    return False

def ids(start, goal, max_depth):  # Iterative Deepening Search
    for depth in range(max_depth):
        visited = set()  # Reset visited set for each depth iteration
        print(f"\nSearching at depth {depth}:")
        if dls(start, goal, depth, visited):
            print(f"Goal node {goal} found at depth {depth}")
            return True
    print(f"Goal node {goal} not found within depth {max_depth}")
    return False

# Driver Code
start_node = '5'
goal_node = '8'
max_depth = 5

print("Following is the Iterative Deepening Search:")
ids(start_node, goal_node, max_depth)
