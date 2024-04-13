import numpy as np
from numba import njit
from heapq import heappop, heappush

@njit
def _dijkstra_shortest_path(grid, source, targets, roughness=None, walls=None):
    # targets is list of one or more nodes
    rows, cols = grid.shape
    visited = np.full((rows, cols), fill_value=False, dtype=np.bool_)
    distance = np.full((rows, cols), fill_value=99999999, dtype=np.float64)
    distance[source[0], source[1]] = 0
    predecessors = {}
    pq = [(0.0, source)]
    closest_target = None

    while pq:
        dist, current = heappop(pq)
        if current in targets:
            closest_target = current
            break
        if visited[current]:
            continue
        visited[current] = True
        cx, cy = current

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[(nx, ny)]:
                    cost = 1 if dx == 0 or dy == 0 else 1.414
                    
                    if roughness is not None:
                        cost *= (1 + roughness[nx, ny])  # Modify cost based on roughness

                    if walls is not None:
                        if walls[nx, ny]:
                            continue
                            
                    new_dist = dist + cost
                    if new_dist < distance[(nx, ny)]:
                        distance[(nx, ny)] = new_dist
                        predecessors[(nx, ny)] = current
                        heappush(pq, (new_dist, (nx, ny)))
                        
    if closest_target is not None:
        path = []
        current = closest_target
        while current != source:
            path.append(current)
            current = predecessors[current]
    
        path.append(source)
        path.reverse()
        return distance, path

    else:
        return distance, None
