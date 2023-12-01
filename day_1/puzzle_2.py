import re


input = 'day_1/puzzle_2.txt'
strings = dict(zip(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], [1, 2, 3, 4, 5, 6, 7, 8, 9]))


def solve(input):
    with open(input) as file:
        lst = []
        for line in file.readlines():
            temp = []
            for k, v in strings.items():
                idxs = re.finditer(pattern=k, string=line)
                for idx in idxs:
                    temp.append((idx.start(), v))
            for idx, val in enumerate(line):
                if val.isdigit():
                    temp.append((idx, int(val)))
            sorted_by_idx = sorted(temp)
            first = str(sorted_by_idx[0][1])
            last = str(sorted_by_idx[-1][1])
            lst.append(int(''.join([first, last])))
    return sum(lst)


if __name__ == '__main__':
    print(solve(input)) #54094