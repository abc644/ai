# 使用chatGPT生成

import random

citys = [
    (0, 3), (0, 0), (0, 2), (0, 1), (1, 0), (1, 3), 
    (2, 0), (2, 3), (3, 0), (3, 3), (3, 1), (3, 2)
]

l = len(citys)
path = [(i+1) % l for i in range(l)]
print("Initial path:", path)

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def path_length(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i + 1) % plen]])
    return dist

print('Initial path length:', path_length(path))

def generate_neighbors(path):
    neighbors = []
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            neighbor = path.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(initial_path):
    current_path = initial_path
    current_length = path_length(current_path)
    
    while True:
        neighbors = generate_neighbors(current_path)
        best_neighbor = min(neighbors, key=path_length)
        best_neighbor_length = path_length(best_neighbor)
        
        if best_neighbor_length >= current_length:
            break
        current_path = best_neighbor
        current_length = best_neighbor_length
    
    return current_path, current_length

final_path, final_length = hill_climbing(path)
print('Final path:', final_path)
print('Final path length:', final_length)
