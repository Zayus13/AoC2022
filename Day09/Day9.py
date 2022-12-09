def get_tail_movement(head_x, head_y, tail_x, tail_y):
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return tail_x, tail_y
    if abs(head_x - tail_x) == 2:
        tail_x = head_x - 1 if head_x > tail_x else head_x + 1
        if abs(head_y - tail_y) == 1:
            return tail_x, head_y
        elif abs(head_y - tail_y) == 2:  # extra case for rope longer than 2
            tail_y = head_y - 1 if head_y > tail_y else head_y + 1
            return tail_x, tail_y
        else:
            return tail_x, tail_y

    if abs(head_y - tail_y) == 2:
        tail_y = head_y - 1 if head_y > tail_y else head_y + 1
        if abs(head_x - tail_x) == 1:
            return head_x, tail_y
        else:
            return tail_x, tail_y


def computed_visited_locations_by_tail(directions, length=2):
    locs = []
    rope = [(0, 0) for _ in range(length)]
    change_x = 0
    change_y = 0
    for direction in directions:
        dir, steps = direction[0], direction[1]
        if dir == "U":
            change_y = 1
            change_x = 0
        if dir == "D":
            change_y = -1
            change_x = 0
        if dir == "L":
            change_y = 0
            change_x = -1
        if dir == "R":
            change_y = 0
            change_x = 1
        for i in range(steps):
            rope[0] = (rope[0][0] + change_x, rope[0][1] + change_y)
            for j in range(1, length):
                rope[j] = get_tail_movement(rope[j - 1][0], rope[j - 1][1], rope[j][0], rope[j][1])
            locs.append(rope[-1])
    return set(locs)


if __name__ == '__main__':
    input = open("day09.txt", "r").read()
    directions = [(line.split()[0], int(line.split()[1])) for line in input.splitlines()]
    res = computed_visited_locations_by_tail(directions)
    print(len(res))
    res = computed_visited_locations_by_tail(directions, 10)
    print(len(res))
