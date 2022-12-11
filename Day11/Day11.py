from pprint import pprint


class Monkey:
    def __init__(self, items, operation, test, t, f):
        self.items = items
        self.operation = operation
        self.test = test
        self.t = t
        self.f = f
        self.counter = 0


    def throw(self, worry_mod, modulo=False):
        item_copy = self.items.copy()
        self.counter += len(item_copy)
        for item in item_copy:
            self.items.remove(item)
            worry = self.operation(item)
            if modulo:
                worry = worry % worry_mod
            else:
                worry = worry // worry_mod

            if worry % self.test == 0:
                self.t.items.append(worry)
            else:
                self.f.items.append(worry)


if __name__ == '__main__':
    data = open("day11.txt", "r").read().split("\n\n")
    monkeys = [Monkey([], None, None, None, None) for i in range(len(data))]
    for config in [(False, 20), (True, 10000)]:
        for i, monkey in enumerate(monkeys):
            monkey_data = data[i].splitlines()
            monkey.items = [int(x) for x in monkey_data[1].split(": ")[1].split(", ")]
            monkey.operation = eval("lambda old: " + monkey_data[2].split("= ")[1])
            monkey.test = int(monkey_data[3].split("by ")[1])
            monkey.t = monkeys[int(monkey_data[4].split(" ")[-1])]
            monkey.f = monkeys[int(monkey_data[5].split(" ")[-1])]

        if not config[0]:
            prod = 3
        else:
            prod = 1
            for monkey in monkeys:
                prod *= monkey.test

        for i in range(config[1]):
            for monkey in monkeys:
                monkey.throw(prod, config[0])

        counters = sorted([monkey.counter for monkey in monkeys], reverse=True)
        print(counters[0] * counters[1])
