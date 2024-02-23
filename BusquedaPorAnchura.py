from collections import deque

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

def bfs(initial_state, goal_state=GOAL_STATE):
    visited = set()
    queue = deque([(initial_state, [])])

    nodes_visited = 0
    max_nodes_in_memory = 0

    while queue:
        current_state, path = queue.popleft()
        nodes_visited += 1

        max_nodes_in_memory = max(max_nodes_in_memory, len(queue))

        if current_state == goal_state:
            return path + [current_state], nodes_visited, max_nodes_in_memory

        visited.add(current_state)

        for direction in ["up", "down", "left", "right"]:
            next_state = move(current_state, direction)
            
            if next_state and next_state not in visited:
                queue.append((next_state, path + [current_state]))

    return None, nodes_visited, max_nodes_in_memory

def print_path(path):
    for state in path:
        for row in state:
            print(' | '.join(str(cell) if cell != 0 else ' ' for cell in row))
        print("------")

if __name__ == "__main__":
    initial = ((2, 4, 6), (5, 0, 7), (8, 1, 3))
    
    path_bfs, bfs_time_complexity, bfs_space_complexity = bfs(initial)
    print("BFS Path:")
    print_path(path_bfs)
    print(f"Complejidad en tiempo (BFS): {bfs_time_complexity} nodos visitados")
    print(f"Complejidad en espacio (BFS): {bfs_space_complexity} nodos máximos en memoria")
