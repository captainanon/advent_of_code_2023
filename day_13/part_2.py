import  copy

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
    r_idx = -1
    c_idx = -1
    i = 0
    break_ = False
    while i < r - 1:
        if pattern[i] == pattern[i+1]:
            temp_count = 1
            j = i - 1
            k = i + 2
            while j >= 0 and k < r:
                if pattern[j] == pattern[k]:
                    temp_count += 1
                    j -= 1
                    k += 1
                else:
                    break
            else: 
                r_idx = i
                break_ = True
                break
        i += 1
    i = 0
    if not break_:
        while i < c - 1:
            if inv_pattern[i] == inv_pattern[i+1]:
                temp_count = 1
                j = i - 1
                k = i + 2
                while j >= 0 and k < c:
                    if inv_pattern[j] == inv_pattern[k]:
                        temp_count += 1
                        j -= 1
                        k += 1
                    else:
                        break
                else: 
                    c_idx = i
                    break
            i += 1
    break_ = False
    for x in range(0, r):
        if break_:
            break
        for y in range(0, c):
            if break_:
                break
            pattern_copy = copy.deepcopy(pattern)
            pattern_copy[x][y] = '.' if pattern[x][y] == '#' else '#'
            inv_pattern = list(zip(*pattern_copy))
            i = 0
            while i < r - 1:
                if pattern_copy[i] == pattern_copy[i+1]:
                    j = i - 1
                    k = i + 2
                    while j >= 0 and k < r:
                        if pattern_copy[j] == pattern_copy[k]:
                            j -= 1
                            k += 1
                        else:
                            break
                    else: 
                        if i != r_idx:
                            count += (i + 1) * 100
                            break_ = True
                            break
                i += 1
            i = 0
            if break_:
                break
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
                        if i != c_idx:
                            count += i + 1
                            break_ = True
                            break
                i += 1
print(count) # 41566
