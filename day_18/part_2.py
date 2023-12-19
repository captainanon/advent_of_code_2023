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
        hex = int(line.split()[-1][2:-2], 16)
        dir = int(line.split()[-1][-2:-1])
        perim += hex
        if dir == 0:
            coord = (coord[0]+hex, coord[1])
        elif dir == 1:
            coord = (coord[0], coord[1]-hex)
        elif dir == 2:
            coord = (coord[0]-hex, coord[1])
        else:
            coord = (coord[0], coord[1]+hex)
        vertices.append(coord)
area_total = int(area(vertices)) + perim // 2 + 1
print(area_total) # 90111113594927