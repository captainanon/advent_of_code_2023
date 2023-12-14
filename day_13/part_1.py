input = 'day_13/input.txt'
with open(input) as file:
    patterns = file.read().split('\n\n')
count = 0
for pattern in patterns:
    pattern_0 = pattern.splitlines()
    pattern = []
    for x in pattern_0:
        pattern.append([y for y in x])
    inv_pattern = list(zip(*pattern))
    r = len(pattern)
    c = len(pattern[0])
    i = 0
    break_ = False
    while i < r - 1:
        if pattern[i] == pattern[i+1]:
            j = i - 1
            k = i + 2
            while j >= 0 and k < r:
                if pattern[j] == pattern[k]:
                    j -= 1
                    k += 1
                else:
                    break
            else: 
                count += (i + 1) * 100
                break_ = True
                break
        i += 1
    i = 0
    if not break_:
        while i < c - 1:
            if inv_pattern[i] == inv_pattern[i+1]:
                j = i - 1
                k = i + 2
                while j >= 0 and k < c:
                    if inv_pattern[j] == inv_pattern[k]:
                        j -= 1
                        k += 1
                    else:
                        break
                else: 
                    count += i+1
                    break
            i += 1
print(count) # 27202
