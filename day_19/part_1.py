input = 'day_19/input.txt'
with open(input) as file:
    workflows, parts = file.read().split('\n\n')
temp = {}
for workflow in workflows.splitlines():
    name, workflow = workflow.split('{')
    workflow = [x.split(':') for x in workflow[:-1].split(',')]
    temp[name] = workflow
sum_ = 0
workflows = temp
for part in parts.splitlines():
    part = part[1:-1].split(',')
    for statement in part:
        exec(statement)
    name = 'in'
    while name not in ('A', 'R'):
        workflow = workflows[name]
        for step in range(len(workflow)-1):
            conditon, name = workflow[step]
            if eval(conditon):
                break
        else:
            name = workflow[-1][0]
    if name == 'A':
        sum_ += sum([int(x[2:]) for x in part])
print(sum_) # 352052