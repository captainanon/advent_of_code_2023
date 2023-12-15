def calc(s):
    init = 0
    for c in s:
        init = ((init + ord(c)) * 17) % 256
    return init


input = 'day_15/input.txt'
with open(input) as file:
    input = file.read().split(',')
sum_ = 0
for s in input:
    sum_ += calc(s)
print(sum_) # 497373