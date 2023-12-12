input = 'day_11/input.txt'
with open(input) as file:
    data = file.read().splitlines()
lines = []
for r in data:
    lines.append([x for x in r])
i = 0
rows = []
while i <len(lines):
    if all([x == '.' for x in lines[i]]):
        rows.append(i)
    i += 1
i = 0
cols = []
while i < len(lines[0]):
    temp = []
    for r in lines:
        temp.append(r[i])
    if all([x == '.' for x in temp]):
        cols.append(i)
    i += 1
i = 1
galaxies = {}
for r, line in enumerate(lines):
    for c, char_ in enumerate(line):
        if char_ == '#':
            galaxies[i] = (r, c)
            i += 1
distance = 0
exp = 1
for i in range(1, len(galaxies)):
    for j in range(i+1, len(galaxies)+1):
        row_exp = len([x for x in rows if x > min(galaxies[i][0], galaxies[j][0]) and x < max(galaxies[i][0], galaxies[j][0])]) * exp
        col_exp = len([x for x in cols if x > min(galaxies[i][1], galaxies[j][1]) and x < max(galaxies[i][1], galaxies[j][1])]) * exp
        distance += abs(galaxies[i][0] - galaxies[j][0]) + row_exp + abs(galaxies[i][1] - galaxies[j][1]) + col_exp
print(distance) # 9799681