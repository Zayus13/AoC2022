from pprint import pprint


def create_structure(input):
    structure = {"name": "/", "children": [], "size": 0}
    current_dir = structure

    for line in input:
        if line.startswith("dir"):
            dir_name = line.split(" ")[1]
            current_dir["children"].append({"name": dir_name, "children": [], "size": 0, "parent": current_dir})

        elif line.startswith("$ cd .."):
            current_dir = current_dir["parent"]

        elif line.startswith("$ cd "):
            dir_name = line.split(" ")[2]
            candidates = [x for x in current_dir["children"] if x["name"] == dir_name]
            if len(candidates) == 1:
                current_dir = candidates[0]

        elif line[0].isdigit():
            size = int(line.split(" ")[0])
            current_dir["size"] += size

    return structure


def get_list_of_sizes(structure):
    sizes = []
    for child in structure["children"]:
        sizes.append(get_size(child))
        sizes.extend(get_list_of_sizes(child))

    return sizes

def get_size(node):
    size = node["size"]
    for child in node["children"]:
        size += get_size(child)

    return size


if __name__ == '__main__':
    input = open("day07.txt").read().splitlines()
    structure = create_structure(input[1:])
    l=get_list_of_sizes(structure)
    print(sum([x for x in l if x <= 100000]))
    current_space = 70000000 - get_size(structure)
    l = [x for x in l if current_space + x >= 30000000]
    l.sort()
    print(l[0])
