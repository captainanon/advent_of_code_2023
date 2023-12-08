from collections import defaultdict
import math

 
input = 'day_8/input.txt'

with open(input) as file:
    map = file.read().splitlines()
directions = map[0]
elements = {}
starting_pos = []
for x in map[2:]:
    temp = x.split('=')
    k = temp[0].strip()
    v = temp[1].strip().split(',')
    v1 = v[0][1:]
    v2 = v[1][1:4]
    elements[k] = (v1, v2)
    if k.endswith('A'):
        starting_pos.append(k)
i = 0
z = defaultdict(lambda: [])
while len(z) < len(starting_pos):
    rl = directions[i % len(directions)]
    for idx, pos in enumerate(starting_pos):    
        if pos.endswith('Z'):
            z[idx].append(i)
        starting_pos[idx] = elements[pos][0 if rl == 'L' else 1]
    i += 1
l = [x[0] for x in z.values()]
lcm_ = math.lcm(*l)

print(lcm_) # 18625484023687