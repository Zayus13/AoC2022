from pprint import pprint


def draw_cave(instructions, xrange, maxy):
    minx = xrange[0]
    cave = [["." for _ in range(xrange[0], xrange[1] + 1)] for x in range(maxy + 1)]
    for line in instructions:
        fx = line[0][0]
        fy = line[0][1]
        sx = line[1][0]
        sy = line[1][1]
        if fx == sx:
            starty, endy = (fy, sy) if fy < sy else (sy, fy)
            for i in range(starty, endy + 1):
                cave[i][fx - minx] = "#"
        if fy == sy:
            startx, endx = (fx - minx, sx - minx) if fx < sx else (sx - minx, fx - minx)
            for i in range(startx, endx + 1):
                cave[fy][i] = "#"
    return cave


def add_sand(cave, startx):
    let_there_be_more_send = True
    counter = 0
    while let_there_be_more_send:
        let_there_be_more_send = let_there_be_more_send and not drop_sand(cave, startx, 0)
        counter += 1
    return counter - 1


def drop_sand(cave, x, y):
    while True:
        if y == len(cave) - 1 or x == 0 or x == len(cave[0]):
            return True
        elif cave[y + 1][x] == ".":
            y = y + 1
        elif y >= 1 and cave[y + 1][x - 1] == ".":
            y = y + 1
            x = x - 1
        elif cave[y + 1][x + 1] == ".":
            y = y + 1
            x = x + 1
        else:
            cave[y][x] = "o"
            return False


def fill_unreadable_places(cave):
    for i in range(1, len(cave)):
        for j in range(1, len(cave[0]) - 1):
            if cave[i - 1][j] == cave[i - 1][j - 1] == cave[i - 1][j + 1] == "#":
                cave[i][j] = "#"
    return cave


def count_fillable_places(cave, startx):
    possible_places = (len(cave)) ** 2
    for i in range(len(cave)):
        for j in range(startx - i, startx + i + 1):
            if j < 0 or j >= len(cave[0]):
                pass
            elif cave[i][j] == "#":
                possible_places -= 1

    return possible_places


if __name__ == '__main__':
    input = open("day14.txt", "r").read().splitlines()
    xs, ys, data = [], [], []
    for i in input:
        i = [(int(j.split(",")[0]), int(j.split(",")[1])) for j in i.split(" -> ")]
        for item in i:
            xs.append(item[0])
            ys.append(item[1])
        i = list(zip(i, i[1:]))
        data = data + i

    minx = min(xs)
    maxx = max(xs)
    maxy = max(ys)
    cave = draw_cave(data, (minx, maxx), maxy)
    pprint(cave, width=500)
    sand_counter = add_sand(cave, 500 - minx)
    pprint(cave, width=500)
    cave_with_floor = draw_cave(data, (minx, maxx), maxy + 1)
    filled_cave = fill_unreadable_places(cave_with_floor)
    pprint(filled_cave, width=500)

    print(sand_counter)
    print(count_fillable_places(filled_cave, 500 - minx))
