from collections import defaultdict


input = 'day_20/input.txt'
with open(input) as file:
    raw = [[y.strip() for y in x.split('->')] for x in file.read().splitlines()]
    raw = [[x, y.split(', ')] for x, y in raw]
graph = {}
modules = {}
conjunctions = defaultdict(lambda: [])
for line in raw:
    neighnbors = line[1]
    if line[0][0] not in '%&':
        type = None
        module = line[0]
        modules[module] = [type, 0]
        graph[module] = neighnbors
    else:
        type = line[0][0]
        module = line[0][1:]
        modules[module] = [type, 0]
        graph[module] = neighnbors
for node, neighnbors in graph.items():
    for neighnbor in neighnbors:
        if neighnbor not in modules.keys():
            continue
        if modules[neighnbor][0] == '&':
            conjunctions[neighnbor].append([node, 0])
high = 0
low = 0
for i in range(0, 1000):
    low += 1
    queue = []
    pulse = 0
    queue.append((pulse, 'broadcaster', 'broadcaster'))
    while queue:
        pulse, node, prev = queue.pop(0)
        if node not in graph.keys():
            continue
        type = modules[node][0]
        if node == 'broadcaster':
            output = 0
        elif type == '%':
            state = modules[node][1]
            if pulse == 0:
                output = 1 if state == 0 else 0
                modules[node][1] = 1 if state == 0 else 0
            else:
                continue
        elif type == '&':
            idx = [x[0] for x in conjunctions[node]].index(prev)
            conjunctions[node][idx][1] = pulse
            state = 1
            for input in conjunctions[node]:
                state *= input[1]
            output = 1 if state == 0 else 0
        for neighnbor in graph[node]:
            high += 1 if output == 1 else 0
            low += 1 if output == 0 else 0
            queue.append((output, neighnbor, node))
print(high * low ) # 938065580
