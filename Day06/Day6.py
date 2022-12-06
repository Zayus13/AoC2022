def find_first_distinct_char_subset(s, length=4):
    for i in range(len(s) - length + 1):
        if len(set(s[i:i + length])) == length:
            return i + length


if __name__ == '__main__':
    with open("day06.txt", "r") as f:
        data = f.readlines()
        res = sum([find_first_distinct_char_subset(line) for line in data])
        res = sum([find_first_distinct_char_subset(line, 14) for line in data])
        print(res)
