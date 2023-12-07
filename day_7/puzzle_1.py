from collections import defaultdict, Counter


input = 'day_7/input.txt'


def solve(input):
    with open(input) as file:
        hands = [x.split() for x in file.read().splitlines()]
        types = []
        for idx, d in enumerate(hands):
            hand = d[0]
            vals = dict(Counter(hand))
            counts = dict(Counter(vals.values()))
            counts = dict(sorted(counts.items(), key=lambda item: item[1]))
            if list(counts.keys())[0] == 2:
                if list(counts.values())[0] == 2:
                    types.append((idx, 2))
                else:
                    types.append((idx, 1))
            types.append((idx, list(counts.keys())[0]))
        pass

        

               
if __name__ == '__main__':
    print(solve(input)) #