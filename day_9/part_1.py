def diff(d):
    temp = []
    for i in range(1, len(d)):
        temp.append(d[i] - d[i-1])
    if not all([x == 0 for x in temp]):
        temp = diff(temp)
    d.append(d[-1]+temp[-1])
    return d


input = 'day_9/input.txt'
with open(input) as file:
    data = file.read().splitlines()
data = [x.split() for x in data]
data = [list(map(int, x)) for x in data]   
s = 0
for idx, line in enumerate(data):
    s += diff(line)[-1]
print(s) # 2175229206