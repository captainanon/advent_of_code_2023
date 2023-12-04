from collections import defaultdict


input = 'day_4/input.txt'


def solve(input):
    cards = defaultdict(lambda: 0)
    with open(input) as file:
        i = 1
        for line in file:
            line = line.strip('\n')
            line = line.split('|')
            winning_nums = [int(x) for x in line[0].split(':')[1].strip().split()]
            my_nums = [int(x) for x in line[1].strip().split()]
            cards[i] += 1
            x = 1
            for num in my_nums:
                if num in winning_nums:
                    cards[i+x] += cards[i]
                    x += 1
            i += 1
    return sum(cards.values())
                

if __name__ == '__main__':
    print(solve(input)) # 6050769