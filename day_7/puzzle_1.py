from collections import defaultdict, Counter


input = 'day_7/input.txt'


def solve(input):
    with open(input) as file:
        hands = [x.split() for x in file.read().splitlines()]
        ordered = []
        result = 0
        for idx, lst in enumerate(hands):
            hand = map_cards(lst[0])
            hands[idx][0] = hand
            vals = dict(Counter(hand))
            counts = dict(Counter(vals.values()))
            counts = dict(sorted(counts.items(), key=lambda item: item[0], reverse=True))
            if list(counts.keys())[0] == 1:
                hands[idx].insert(0, 1)
            elif list(counts.keys())[0] == 2 and list(counts.values())[0] == 1:
                hands[idx].insert(0, 2)
            elif list(counts.keys())[0] == 2 and list(counts.values())[0] == 2:
                hands[idx].insert(0, 3)
            elif list(counts.keys())[0] == 3 and list(counts.keys())[1] == 1:
                hands[idx].insert(0, 4)
            elif list(counts.keys())[0] == 3 and list(counts.keys())[1] == 2:
                hands[idx].insert(0, 5)
            elif list(counts.keys())[0] == 4:
                hands[idx].insert(0, 6)
            elif list(counts.keys())[0] == 5:
                hands[idx].insert(0, 7)
    bubble_sort_by_type(hands)
    for i in range(1, 8):
        subset = list(filter(lambda x: x[0] == i, hands))
        if subset != []:
            ordered.extend(bubble_sort_by_hand(subset))
    for i in range(len(ordered)):
        result += (i + 1) * int(ordered[i][2])
    return result
        

def map_cards(hand):
    original_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    new_cards =      ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n']
    map_dict = dict(zip(original_cards, new_cards))
    for i in hand:
        if i in map_dict.keys():
            hand=hand.replace(i, map_dict[i])
    return hand
        

def bubble_sort_by_type(hands):
    for i in range(len(hands)):
        for j in range(0, len(hands) - i - 1):
            if hands[j][0] > hands[j + 1][0]:
                temp = hands[j]
                hands[j] = hands[j+1]
                hands[j+1] = temp


def bubble_sort_by_hand(subset):
    for i in range(len(subset)):
        for j in range(0, len(subset) - i - 1):
            if subset[j][1] > subset[j + 1][1]:
                temp = subset[j]
                subset[j] = subset[j+1]
                subset[j+1] = temp
    return subset

               
if __name__ == '__main__':
    print(solve(input)) # 247815719