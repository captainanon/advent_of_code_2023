from queue import Queue


def calc(node, grid):
    r = len(grid)
    c = len(grid[0])
    q = Queue(maxsize=r*c)
    q.put(node)
    energized = set()
    splits = set()
    while not q.empty():
        x, y, dir = q.get()
        path = set()
        while (x, y, dir) not in path and x >= 0 and x < r and y >= 0 and y < c:
            energized.add((x, y))
            path.add((x, y, dir))
            if grid[x][y] == '.' and dir in (-1, 1):
                next = (x, y+dir, dir)
            elif grid[x][y] == '.' and dir in (-2, 2):
                next = (x-dir//2, y, dir)
            elif grid[x][y] == '-' and dir in (-1, 1):
                next = (x, y+dir, dir)
            elif grid[x][y] == '-' and dir in (-2, 2):
                next = (x, y+1, 1)
                if (x, y-1, -1) not in splits:
                    q.put((x, y-1, -1))
                    splits.add((x, y-1, -1))
            elif grid[x][y] == '|' and dir in (-2, 2):
                next = (x-dir//2, y, dir)
            elif grid[x][y] == '|' and dir in (-1, 1):
                next = (x+1, y, -2)
                if (x-1, y, 2) not in splits:
                    q.put((x-1, y, 2))
                    splits.add((x-1, y, 2))
            elif grid[x][y] == '\\':
                if dir == 1:
                    next = (x+1, y, -2)
                elif dir == -1:
                    next = (x-1, y, 2)
                elif dir == 2:
                    next = (x, y-1, -1)
                elif dir == -2:
                    next = (x, y+1, 1)
            elif grid[x][y] == '/':
                if dir == 1:
                    next = (x-1, y, 2)
                elif dir == -1:
                    next = (x+1, y, -2)
                elif dir == 2:
                    next = (x, y+1, 1)
                elif dir == -2:
                    next = (x, y-1, -1)
            x = next[0]
            y = next[1]
            dir = next[2]
    return len(energized)


input = 'day_16/input.txt'
with open(input) as file:
    input = file.read().splitlines()
grid = [[x for x in y] for y in input]
r = len(grid)
c = len(grid[0])
nodes = []
for y in range(0, c):
    nodes.append((0, y, -2))
for y in range(0, c):
    nodes.append((r-1, y, 2))
for x in range(0, r):
    nodes.append((x, 0, 1))
for x in range(0, r):
    nodes.append((x, c-1, -1))
max_ = 0
for node in nodes:
    max_ = max(max_, calc(node, grid))
print(max_) # 8163