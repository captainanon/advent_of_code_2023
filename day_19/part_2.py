import copy


def solve(node, x, m, a, s, x_, m_, a_, s_):
    global sum_
    if node[1] not in ('A', 'R'):
        for idx, neighbour in enumerate(graph[node[1]]):
            if neighbour[0] is not None:
                rating = neighbour[0][0]
                op = neighbour[0][1]
                num = int(neighbour[0][2:])
                if rating == 'x':
                    if op == '>':
                        x = set([i for i in x if i > num])
                        x_ = set([i for i in x_ if i <= num])
                    else:
                        x = set([i for i in x if i < num])
                        x_ = set([i for i in x_ if i >= num])
                elif rating == 'm':
                    if op == '>':
                        m = set([i for i in m if i > num])
                        m_ = set([i for i in m_ if i <= num])
                    else:
                        m = set([i for i in m if i < num])
                        m_ = set([i for i in m_ if i >= num])
                elif rating == 'a':
                    if op == '>':
                        a = set([i for i in a if i > num])
                        a_ = set([i for i in a_ if i <= num])
                    else:
                        a = set([i for i in a if i < num])
                        a_ = set([i for i in a_ if i >= num])
                elif rating == 's':
                    if op == '>':
                        s = set([i for i in s if i > num])
                        s_ = set([i for i in s_ if i <= num])
                    else:
                        s = set([i for i in s if i < num])
                        s_ = set([i for i in s_ if i >= num])
            if neighbour[1] == 'A':
                sum_ += len(x) * len(m) * len(a) * len(s)
            if idx == 0:
                solve(neighbour, x, m, a, s, x_, m_, a_, s_)
            else:
                x = copy.deepcopy(x_)
                m = copy.deepcopy(m_)
                a = copy.deepcopy(a_)
                s = copy.deepcopy(s_)
                solve(neighbour, x, m, a, s, x_, m_, a_, s_)


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
x_= set(range(1, 4001))
m_ = set(range(1, 4001))
a_ = set(range(1, 4001))
s_ = set(range(1, 4001))
sum_ = 0
solve((None, 'in'), x, m, a, s, x_, m_, a_, s_)
print(sum_)
287985651300000
167409079868000