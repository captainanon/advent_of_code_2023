def solve(node, x, m, a, s, sum_):
    if node[0] is not None:
        rating = node[0][0]
        op = node[0][1]
        num = int(node[0][2:])
        if rating == 'x':
            if op == '>':
                x = set([i for i in x if i > num])
            else:
                x = set([i for i in x if i < num])
        elif rating == 'm':
            if op == '>':
                m = set([i for i in m if i > num])
            else:
                m = set([i for i in m if i < num])
        elif rating == 'a':
            if op == '>':
                a = set([i for i in a if i > num])
            else:
                a = set([i for i in a if i < num])
        elif rating == 's':
            if op == '>':
                s = set([i for i in s if i > num])
            else:
                s = set([i for i in s if i < num])
    if node[1] == 'A':
        sum_ += len(x) * len(m) * len(a) * len(s)
    cache_ = []
    if node[1] not in ('A', 'R'):
        for idx, neighbor in enumerate(graph[node[1]]):
            if neighbor[0] is not None:
                cache_.append(neighbor[0])       
            if idx == 0:
                sum_ = solve(neighbor, x, m, a, s, sum_)
            else:
                for i in range(idx):
                    expression = cache_[i]
                    rating = expression[0]
                    op = expression[1]
                    num = int(expression[2:])
                    if rating == 'x':
                        if op == '>':
                            x = set([i for i in x if i <= num])
                        else:
                            x = set([i for i in x if i >= num])
                    if rating == 'm':
                        if op == '>':
                            m = set([i for i in m if i <= num])
                        else:
                            m = set([i for i in m if i >= num])
                    if rating == 'a':
                        if op == '>':
                            a = set([i for i in a if i <= num])
                        else:
                            a = set([i for i in a if i >= num])
                    if rating == 's':
                        if op == '>':
                            s = set([i for i in s if i <= num])
                        else:
                            s = set([i for i in s if i >= num])
                sum_ = solve(neighbor, x, m, a, s, sum_)
    return sum_


input = 'day_19/input.txt'
with open(input) as file:
    workflows, _ = file.read().split('\n\n')
graph = {}
for workflow in workflows.splitlines():
    name, workflow = workflow.split('{')
    workflow = [x.split(':') for x in workflow[:-1].split(',')]
    graph[name] = [(k, v) for k, v in  workflow[:-1]]
    graph[name].append((None, workflow[-1][0]))
x = set(range(1, 4001))
m = set(range(1, 4001))
a = set(range(1, 4001))
s = set(range(1, 4001))
sum_ = 0
start = (None, 'in')
sum_ = solve(start, x, m, a, s, sum_)
print(sum_) # 116606738659695