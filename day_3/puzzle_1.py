input = 'day_3/input.txt'


def solve(input):
    schematic = []
    with open(input) as file:
        for line in file:
            line = line.strip('\n')
            schematic.append(line)
    l = len(schematic)
    w = len(schematic[0])
    r = 0
    sum_ = 0
    while r < l:
        c = 0
        while c < w:
            if schematic[r][c].isdigit():
                c, num, bool_ = is_part_number(schematic, r, c)
                if bool_:
                    sum_ += num
                c += 1
            else:
                c += 1
        r += 1
    return sum_


def is_part_number(schematic, r, c):  
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
            if (idx >= c_left and idx <= c_right) and (not char_.isdigit() and char_ != '.'):
                return c, num, True
    if c_left >= 0 and (not schematic[r][c_left].isdigit() and schematic[r][c_left] != '.'):
        return c, num, True
    if c_right < w and (not schematic[r][c_right].isdigit() and schematic[r][c_right] != '.'):
        return c, num, True
    if r_below < l:
        for idx, char_ in enumerate(schematic[r_below]):
            if (idx >= c_left and idx <= c_right) and (not char_.isdigit() and char_ != '.'):
                return c, num, True
    return c, num, False


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


if __name__ == '__main__':
    print(solve(input)) # 514969