input = 'day_10/input.txt'


def is_loop(prev, node):
    result = False
    while True:
        path.append(node)
        type = data[node[0]][node[1]]
        if node == start:
                result = True
                break
        if node[0] - prev[0] == 1:
            if type == '|':
                if node[0] + 1 < r:
                    next = (node[0]+1, node[1])
                    if data[next[0]][next[1]] not in ('|', 'L', 'J', 'S'):
                        break
                else:
                    break
            elif type == 'L':
                if node[1] + 1 < c:
                    next = (node[0], node[1]+1)
                    if data[next[0]][next[1]] not in ('-', 'J', '7', 'S'):
                        break
                else:
                    break
            elif type == 'J':
                if node[1] - 1 >= 0:
                    next = (node[0], node[1]-1)
                    if data[next[0]][next[1]] not in ('-', 'L', 'F', 'S'):
                        break
                else:
                    break
            prev = node
            node = next
            continue
        elif node[0] - prev[0] == -1:
            if type == '|':
                if node[0] - 1 >= 0:
                    next = (node[0]-1, node[1])
                    if data[next[0]][next[1]] not in ('|', '7', 'F', 'S'):
                        break
                else:
                    break
            elif type == '7':
                if node[1] - 1 >= 0:
                    next = (node[0], node[1]-1)
                    if data[next[0]][next[1]] not in ('-', 'L', 'F', 'S'):
                        break
                else:
                    break
            elif type == 'F':
                if node[1] + 1 < c:
                    next = (node[0], node[1]+1)
                    if data[next[0]][next[1]] not in ('-', 'J', '7', 'S'):
                        break
                else:
                    break
            prev = node
            node = next
            continue
        elif node[1] - prev[1] == -1:
            if type == '-':
                if node[1] - 1 >= 0:
                    next = (node[0], node[1]-1)
                    if data[next[0]][next[1]] not in ('-', 'L', 'F', 'S'):
                        break
                else:
                    break
            elif type == 'L':
                if node[0] - 1 >= 0:
                    next = (node[0]-1, node[1])
                    if data[next[0]][next[1]] not in ('|', '7', 'F', 'S'):
                        break
                else:
                    break
            elif type == 'F':
                if node[0] + 1 < r:
                    next = (node[0]+1, node[1])
                    if data[next[0]][next[1]] not in ('|', 'L', 'J', 'S'):
                        break
                else:
                    break
            prev = node
            node = next
            continue
        elif node[1] - prev[1] == 1:
            if type == '-':
                if node[1] + 1 < c:
                    next = (node[0], node[1]+1)
                    if data[next[0]][next[1]] not in ('-', 'J', '7', 'S'):
                        break
                else:
                    break
            elif type == 'J':
                if node[0] - 1 >= 0:
                    next = (node[0]-1, node[1])
                    if data[next[0]][next[1]] not in ('|', '7', 'F', 'S'):
                        break
                else:
                    break
            elif type == '7':
                if node[0] + 1 < r:
                    next = (node[0]+1, node[1])
                    if data[next[0]][next[1]] not in ('|', 'L', 'J', 'S'):
                        break
                else:
                    break
            prev = node
            node = next
            continue
    return result


coords = []
with open(input) as file:
    data = file.read().splitlines()
for r, line in enumerate(data):
    temp = []
    for c, char_ in enumerate(line):
        temp.append((r, c))
        if char_ == 'S':
            start = (r, c)
    coords.append(temp)
r = len(data)
c = len(data[0])
for idx, neighbor in enumerate([data[start[0]][start[1]+1], data[start[0]-1][start[1]], data[start[0]][start[1]-1], data[start[0]+1][start[1]]]):
    path = [start]
    if idx == 0 and neighbor in ('-', 'J', '7'):
        if is_loop(start, (start[0], start[1]+1)):
            break
    elif idx == 1 and neighbor in ('|', 'L', 'J'):
        if is_loop(start, (start[0]-1, start[1])):
            break
    elif idx == 2 and neighbor in ('-', 'L', 'F'):
        if is_loop(start, (start[0], start[1]-1)):
            break
    elif idx == 3 and neighbor in ('|', '7', 'F'):
        if is_loop(start, (start[0]+1, start[1])):
            break

throw_out = set()
for row in coords:
    for coord in row:
        if coord in path:
            throw_out.add(coord)
            continue
        count = 0
        while coord[1] < c:
            coord = (coord[0], coord[1]-1)
            type = data[coord[0]][coord[1]]
            if coord in path and type == '|':
                count += 1
            
print(result) # 6823