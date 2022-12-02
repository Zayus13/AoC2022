def get_max_in_list(data, k=1):
    res = []
    maxi = 0
    for i in data:
        if i == "":
            res.append(maxi)
            maxi = 0
        else:
            maxi = maxi + int(i)
    res.append(maxi)
    res.sort()
    return res[-k:]


if __name__ == '__main__':
    file = open("day01.txt", "r")
    data = [list_item.strip() for list_item in file.readlines()]
    print(sum(get_max_in_list(data, 1)))
    print(sum(get_max_in_list(data, 3)))