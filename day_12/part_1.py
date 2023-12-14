import itertools
from collections import defaultdict
from operator import itemgetter


input = 'day_12/input.txt'
with open(input) as file:
    lines = file.read().splitlines()
records = []
for line in lines:
    temp = line.split()
    records.append([temp[0], [int(x) for x in temp[1].split(',')]])
s = 0
for record in records:
    n = len(record[0])
    orig = record[0]
    pattern = record[1]
    perms = set()
    idxs = [idx for idx, val in enumerate(orig) if val != '?']
    if idxs != []:
        search_space = [''.join(x) for x in itertools.product('.#', repeat=n) if ''.join(itemgetter(*idxs)(orig)) == ''.join(itemgetter(*idxs)(''.join(x)))]
    else:
        search_space = [''.join(x) for x in itertools.product('.#', repeat=n)]
    for perm in search_space:
        i = 0
        counts = defaultdict(lambda: 0)
        for idx, char_ in enumerate(perm):
            if char_ == '#':
                counts[i] += 1
            else:
                i += 1
        else:
            if list(counts.values()) == pattern:
                perms.add(perm)
    s += len(perms)
print(s)
