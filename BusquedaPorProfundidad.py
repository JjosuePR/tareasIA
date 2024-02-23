GOAL_STATE = ((0, 8, 7), (6, 5, 4), (3, 2, 1))

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state, direction):
    i, j = find_blank(state)
    new_state = [list(row) for row in state]

    if direction == "up" and i > 0:
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
    elif direction == "down" and i < 2:
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
    elif direction == "left" and j > 0:
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
    elif direction == "right" and j < 2:
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
    else:
        return None

    return tuple(map(tuple, new_state))

def dfs(initial_state, goal_state=GOAL_STATE, depth_limit=1000):
    visited = set()
    stack = [(initial_state, [])]

    nodes_visited = 0
    max_nodes_in_memory = 0

    while stack:
        current_state, path = stack.pop()
        nodes_visited += 1

        max_nodes_in_memory = max(max_nodes_in_memory, len(stack))

        if current_state == goal_state:
            return path + [current_state], nodes_visited, max_nodes_in_memory

        if len(path) > depth_limit:
            continue

        visited.add(current_state)

        for direction in ["up", "down", "left", "right"]:
            next_state = move(current_state, direction)

            if next_state and next_state not in visited:
                stack.append((next_state, path + [current_state]))

    return None, nodes_visited, max_nodes_in_memory

def print_path(path):
    for state in path:
        for row in state:
            print(' | '.join(str(cell) if cell != 0 else ' ' for cell in row))
        print("------")

if __name__ == "__main__":
    initial = ((2, 4, 6), (5, 0, 7), (8, 1, 3))
    path_dfs, dfs_time_complexity, dfs_space_complexity = dfs(initial)
    print("DFS Path:")
    print_path(path_dfs)
    print(f"Complejidad en tiempo (DFS): {dfs_time_complexity} nodos visitados")
    print(f"Complejidad en espacio (DFS): {dfs_space_complexity} nodos máximos en memoria")
