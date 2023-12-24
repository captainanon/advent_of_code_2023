import numpy as np
import copy


input = 'day_21/input.txt'
with open(input) as file:
    map = file.read().splitlines()
    orig_map = copy.deepcopy(map)
    temp = []
    n_rep = 9
    for line in map:
        temp.append(line * n_rep)
    map = temp * n_rep
    s_locs = []
    for r, row in enumerate(map):
      for c, val in enumerate(row):
        if val == 'S':
            s_locs.append((r, c))
start = s_locs[n_rep**2 // 2]
rows = len(map)
cols = len(map[0])
step = 0
count = 0
r, c = start
visited = set()
queue = []
queue.append((0, r, c))
visited.add((0, r, c))
x = []
y = []
elf_steps = 26501365
periodicity = len(orig_map )
offest = elf_steps % periodicity
for steps in range(1, periodicity * 2 + offest + 1):
    while queue and step <= steps:
        step, r, c = queue.pop(0)
        step += 1
        neighbours = [(r, c) for r, c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if 0 <= r < rows and 0 <= c < cols and map[r][c] in ['S', '.']]
        for r, c in neighbours:
            if (step, r, c) not in visited:
                visited.add((step, r, c))
                queue.append((step, r, c))
    num = len([(y, z) for x, y, z in visited if x == steps])
    if steps in range(offest, periodicity * 2 + offest + 1, periodicity):
        x.append(steps)
        y.append(num)
z = np.poly1d(np.polyfit(x,y,2))
print(round(z(elf_steps))) # 602259568764234