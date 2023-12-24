input = 'day_21/input.txt'
with open(input) as file:
    map = file.read().splitlines()
    for r, row in enumerate(map):
      for c, val in enumerate(row):
        if val == 'S':
            start = (r, c)
rows = len(map)
cols = len(map[0])
step = 0
steps = 64
r, c = start
visited = set()
queue = []
queue.append((0, r, c))
visited.add((0, r, c))
while queue and step <= steps:
    step, r, c = queue.pop(0)
    step += 1
    neighbours = [(r, c) for r, c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if 0 <= r < rows and 0 <= c < cols and map[r][c] in ['S', '.']]
    for r, c in neighbours:
        if (step, r, c) not in visited:
            visited.add((step, r, c))
            queue.append((step, r, c))
num = len([(y, z) for x, y, z in visited if x == steps])
print(num) # 3615
