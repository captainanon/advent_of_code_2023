input = 'day_3/input.txt'
gear_dict = {}


def solve(input):
    schematic = []
    with open(input) as file:
        for line in file:
            line = line.strip('\n')
            schematic.append(line)
    get_gear_idxs(schematic)
    l = len(schematic)
    w = len(schematic[0])
    r = 0
    sum_ = 0
    while r < l:
        c = 0
        while c < w:
            if schematic[r][c].isdigit():
                c = is_gear_number(schematic, r, c)
                c += 1
            else:
                c += 1
        r += 1
    return calc_gears()


def get_gear_idxs(schematic):
    l = len(schematic)
    w = len(schematic[0])
    r = 0
    while r < l:
        c = 0
        while c < w:
            if schematic[r][c] == '*':
                gear_dict[(r, c)] = []
                c += 1
            else:
                c += 1
        r += 1


def is_gear_number(schematic, r, c):  
    c0 = c
    num, c = get_number(schematic, r, c)   
    l = len(schematic)
    w = len(schematic[0])
    r_above = r - 1
    r_below = r + 1
    c_left = c0 - 1
    c_right = c + 1
    if r_above >= 0:
        for idx, char_ in enumerate(schematic[r_above]):
            if (idx >= c_left and idx <= c_right) and char_ == '*':
                gear_dict[(r_above, idx)].append(num)
                return c
    if c_left >= 0 and schematic[r][c_left] == '*':
        gear_dict[(r, c_left)].append(num)
        return c
    if c_right < w and schematic[r][c_right] == '*':
        gear_dict[(r, c_right)].append(num)
        return c
    if r_below < l:
        for idx, char_ in enumerate(schematic[r_below]):
            if (idx >= c_left and idx <= c_right) and char_ == '*':
                gear_dict[(r_below, idx)].append(num)
                return c
    return c


def get_number(schematic, r, c):
    w = len(schematic[0])
    num = []
    while schematic[r][c].isdigit():
        num.append(schematic[r][c])
        if c + 1 < w:
            c += 1
        else:
            return int(''.join(num)), c
    return int(''.join(num)), c - 1


def calc_gears():
    result = 0
    for idx, gears in gear_dict.items():
        if len(gears) == 2:
            result += gears[0] * gears[1]
    return result


if __name__ == '__main__':
    print(solve(input)) # 78915902