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


input = 'day_18/input.txt'
with open(input) as file:
    lines = file.read().splitlines()
    coord = (0, 0)
    vertices = []
    perim = 0
    for line in lines:
        val = int(line.split()[1])
        dir = line.split()[0]
        perim += val
        if dir == 'R':
            coord = (coord[0]+val, coord[1])
        elif dir == 'D':
            coord = (coord[0], coord[1]-val)
        elif dir == 'L':
            coord = (coord[0]-val, coord[1])
        else:
            coord = (coord[0], coord[1]+val)
        vertices.append(coord)
area_total = int(area(vertices)) + perim // 2 + 1
print(area_total) # 40745