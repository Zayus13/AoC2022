def check_inclusion(range1, range2):
    if (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range1[0] >= range2[0] and range1[1] <= range2[1]):
        return 1
    else:
        return 0

def check_overlap(range1, range2):
    if (range1[0] <= range2[0] and range1[1] >= range2[0]) or (range1[0] <= range2[1] and range1[1] >= range2[1]):
        return 1
    else:
        return 0 + check_inclusion(range1, range2)


if __name__ == '__main__':
    with open("day04.txt", "r") as f:
        data = f.readlines()
        inclusions = 0
        overlaps = 0
        for i in data:
            range1 = [int(j) for j in i.split(",")[0].split("-")]
            range2 = [int(j) for j in i.split(",")[1].split("-")]
            inclusions += check_inclusion(range1, range2)
            overlaps += check_overlap(range1, range2)
        print(inclusions)
        print(overlaps)
