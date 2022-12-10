def add_20_plus_40n(additions):
    counter = 0
    strength = 1
    result = 0
    res_string = ""
    for i, addition in enumerate(additions):
        if abs(counter % 40 - strength) <= 1:
            res_string += "#"
        else:
            res_string += "."
        counter += 1
        if (counter + 20) % 40 == 0:
            result += counter * strength

        if addition:
            if abs(counter % 40 - strength) <= 1:
                res_string += "#"
            else:
                res_string += "."
            counter += 1
            if (counter + 20) % 40 == 0:
                result += counter * strength
            strength += addition

    return result, res_string


if __name__ == '__main__':
    data = open("day10.txt", "r").read().splitlines()
    additions = [int(line.split()[1]) if line.split()[0] == 'addx' else None for line in data]
    res1, res2 = add_20_plus_40n(additions)
    print(res1)
    print("\n".join([res2[i:i + 40] for i in range(0, len(res2), 40)]))

"""
###..#....####.####.#..#.#....###..###..
#..#.#....#....#....#..#.#....#..#.#..#.
#..#.#....###..###..#..#.#....#..#.###..
###..#....#....#....#..#.#....###..#..#.
#....#....#....#....#..#.#....#....#..#.
#....####.####.#.....##..####.#....###..
"""