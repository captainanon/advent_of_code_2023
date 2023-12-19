from queue import PriorityQueue
from collections import defaultdict


def get_neighbors(r, c, dr, dc, n):
    neighbors = set()
    if  n < 10 and (dr, dc) != (0, 0):
        nr =  r + dr
        nc =  c + dc
        if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
            neighbors.add((nr, nc, dr, dc, n+1))
    if 4 <= n or (dr, dc) == (0, 0):
        for ndr, ndc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                    neighbors.add((nr, nc, ndr, ndc, 1))
    return neighbors - visited


input = 'day_17/input.txt'
with open(input) as file:
    graph = [[int(x) for x in y] for y in file.read().splitlines()]
visited = set()
start = (0, 0, 0, 0, 0, 0)
cache_ = defaultdict(lambda: float('inf'))
cache_[start[1:]] = 0
pq = PriorityQueue()
pq.put(start)
while not pq.empty():
    hl, r, c, dr, dc, n = pq.get()
    visited.add((r, c, dr, dc, n))
    for nr, nc, ndr, ndc, nn in get_neighbors(r, c, dr, dc, n):
        nhl = graph[nr][nc]
        old = cache_[(nr, nc, ndr, ndc, nn )]
        new = hl + nhl 
        if new < old:
            pq.put((hl + nhl, nr, nc, ndr, ndc, nn))
            cache_[(nr, nc, ndr, ndc, nn )] = new
result_dict = {k: v for k, v in cache_.items() if k[0] == len(graph)-1 and k[1] == len(graph[0])-1 and k[4] >= 4}
result = sorted(result_dict.items(), key=lambda x: x[1])[0][1]
print(result) # 993