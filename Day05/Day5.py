import re


def get_start_config(data):
    lines = []
    for line in data.splitlines():
        if (line.strip().startswith("1")):
            break
        line = line.replace("    ", " [ ]")
        line = re.findall(r"\[(.)\]", line)
        lines.append(line)
    lines.reverse()
    stacks = [[] for _ in range(len(lines[0]))]
    for line in lines:
        for i, c in enumerate(line):
            if c != " ":
                stacks[i].append(c)
    return stacks


def transform_stacks(stacks, src, dest, amount, multi=False):
    if not multi:
        stacks[dest] = stacks[dest] + stacks[src][:-amount - 1:-1]
        stacks[src] = stacks[src][:-amount]
    else:
        stacks[dest] = stacks[dest] + stacks[src][-amount:]
        stacks[src] = stacks[src][:-amount]


if __name__ == '__main__':
    with open("day05.txt", "r") as f:
        data = f.read()
    for case in [True, False]:
        stacks = get_start_config(data)
        for line in data.splitlines():
            if (line.startswith("move")):
                amount, src, dest = map(int, re.findall(r"\d+", line))
                transform_stacks(stacks, src - 1, dest - 1, amount, case)
        print("".join([stack[-1] for stack in stacks]))
