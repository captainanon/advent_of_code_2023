def area(v):
    n = len(v)
    s1 = 0
    s2 = 0
    for i in range(0, n-1):
        s1 += v[i][0] *  v[i+1][1]
        s2 += v[i+1][0] * v[i][1]
    s1 += v[n-1][0] * v[0][1]   
    s2 += v[0][0] * v[n-1][1]   
    area = abs(s1 - s2) / 2
    return area


def is_loop(prev, node):
    result = False
    while True:
        path.append(node)
        type = data[node[0]][node[1]]
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
            if next == start:
                result = True
                break
            else:
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
            if next == start:
                result = True
                break
            else:
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
            if next == start:
                result = True
                break
            else:
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
            if next == start:
                result = True
                break
            else:
                prev = node
                node = next
                continue
    return result


input = 'day_10/input.txt'
with open(input) as file:
    data = file.read().splitlines()
for r, line in enumerate(data):
    for c, char_ in enumerate(line):
        if char_ == 'S':
            start = (r, c)
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
perimeter = len(path)
total_area = area(path)
interior_area = total_area - perimeter / 2 + 1
print(int(interior_area)) # 415