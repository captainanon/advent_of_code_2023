from collections import defaultdict


def hash(s):
    init = 0
    for c in s:
        init = ((init + ord(c)) * 17) % 256
    return init


input = 'day_15/input.txt'
with open(input) as file:
    input = file.read().split(',')
d = defaultdict(lambda: [])
sum_ = 0
for s in input:
    if '-' in s:
        label, lens  = s.split('-')
        box = hash(label)
        for idx, item in enumerate(d[box]):
            if label in item.keys():
                d[box].pop(idx)
                break
    elif '=' in s:
        label, lens = s.split('=')
        box = hash(label)
        for idx, item in enumerate(d[box]):
            if label in item.keys():
                d[box][idx][label] = lens
                break
        else:
            d[box].append({label: lens})
sum_ = 0
for box_num, box in d.items():
    for slot_num, _ in enumerate(box):
        sum_ += (1 + box_num) * (slot_num + 1) * int(list(box[slot_num].values())[0])
print(sum_) # 259356