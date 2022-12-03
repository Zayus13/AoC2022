def find_and_value_duplicate(s1, s2, s3 = None):
    for j in s1:
        if j in s2:
            if s3 is None or j in s3:
                value = ord(j)
                if ord('A') <= value <= ord('Z'):
                    return 26 + value - ord('A') + 1
                elif ord('a') <= value <= ord('z'):
                    return value - ord('a') + 1
                else:
                    print("Error: invalid character")
                    return 0


if __name__ == '__main__':
    with open("day03.txt", "r") as f:
        data = f.readlines()
        res1 = sum([find_and_value_duplicate(line[:len(line) // 2], line[len(line) // 2:]) for line in data])
        print(res1)

        res2 = 0
        i = 0
        while i < len(data):
            res2 += find_and_value_duplicate(data[i], data[i + 1], data[i + 2])
            i = i + 3
        print(res2)
