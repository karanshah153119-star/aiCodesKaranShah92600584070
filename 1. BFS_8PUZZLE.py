#Student Name :- karan shah
#Student Enrollment No :- 92600584070
from itertools import permutations
dist = [
         [0 ,10 ,15 , 20],
         [10 ,0 ,35 , 25],
         [15 ,35 ,0 , 30],
         [20 ,25 ,30 , 0]
    ]
cities = ['A','B','C','D']
n = len(dist)

min_cost = float('inf')
best_path = []
for path in permutations(range(1,n)):
    cost = 0
    current = 0

    for city in path:
        cost = cost + dist[current][city]
        current = city
    cost = cost + dist[current][0]

    if cost < min_cost:
        min_cost = cost
        best_path = (0,) + path + (0,)
route = []
for i in best_path:
    route.append(cities[i])

print("Shortest path:","->".join(route))
print("Minimum cost:",min_cost)
# Goal state 
goal = (1, 2, 3, 
        4, 5, 6,
        7, 8, 0)

# Function to print the puzzle
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()
    
# Generate all possible moves
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)   #position of blank/zero
    row, col = divmod(zero, 3)
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP DOWN LEFT RIGHT
    
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            
            neighbors.append(tuple(new_state))
            
    return neighbors

def bfs(start):
    queue = [(start, [])]
    visited = set()
    
    while queue:
        state, path = queue.pop(0)
        
        if state in visited:
            continue
        
        visited.add(state)
        
        if state == goal:
            return path + [state]
        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path + [start]))
                
    return None

# Example start state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = bfs(start)  

if solution:
    print("Solution Found in", len(solution)-1, "moves:\n")
    
    for step in solution:
        print_board(step)
        
else:
    print("No solution Found.")
    
