input = 'day_8/input.txt'


with open(input) as file:
    map = file.read().splitlines()
directions = map[0]
elements = {}
for x in map[2:]:
    temp = x.split('=')
    k = temp[0].strip()
    v = temp[1].strip().split(',')
    v1 = v[0][1:]
    v2 = v[1][1:4]
    elements[k] = (v1, v2)
l = len(directions)
i = 0
element = 'AAA'
while element != 'ZZZ':
    rl = directions[i % l]
    element = elements[element][0 if rl == 'L' else 1]
    i += 1


print(i) # 17287