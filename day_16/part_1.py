from queue import Queue


input = 'day_16/input.txt'
with open(input) as file:
    input = file.read().splitlines()
grid = [[x for x in y] for y in input]
r = len(grid)
c = len(grid[0])
q = Queue(maxsize=r*c)
q.put((0, 0, 1))
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
count = len(energized)
print(count) # 6816