from queue import PriorityQueue


def find_index_2d(matrix, value):
    for i, row in enumerate(matrix):
        if value in row:
            return i, row.index(value)


def astar(matrix, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(node):
        neighbors = []
        if node[0] > 0 and matrix[node[0] - 1][node[1]] - matrix[node[0]][node[1]] <= 1:
            neighbors.append((node[0] - 1, node[1]))
        if node[0] < len(matrix) - 1 and matrix[node[0] + 1][node[1]] - matrix[node[0]][node[1]] <= 1:
            neighbors.append((node[0] + 1, node[1]))
        if node[1] > 0 and matrix[node[0]][node[1] - 1] - matrix[node[0]][node[1]] <= 1:
            neighbors.append((node[0], node[1] - 1))
        if node[1] < len(matrix[0]) - 1 and matrix[node[0]][node[1] + 1] - matrix[node[0]][node[1]] <= 1:
            neighbors.append((node[0], node[1] + 1))
        return neighbors

    p = PriorityQueue()

    p.put((0, start, 0))
    visited = set()
    while not p.empty():
        cost, (x, y), counter = p.get()
        if (x, y) == end:
            return counter
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for neighbor in get_neighbors((x, y)):
            p.put((counter + 1 + heuristic(neighbor, end), neighbor, counter + 1))
    return -1


def part2(matrix, end):
    def get_neighbors_inverse(node):
        neighbors = []
        if node[0] > 0 and -1 <= matrix[node[0] - 1][node[1]] - matrix[node[0]][node[1]]:
            neighbors.append((node[0] - 1, node[1]))
        if node[0] < len(matrix) - 1 and -1 <= matrix[node[0] + 1][node[1]] - matrix[node[0]][node[1]]:
            neighbors.append((node[0] + 1, node[1]))
        if node[1] > 0 and -1 <= matrix[node[0]][node[1] - 1] - matrix[node[0]][node[1]]:
            neighbors.append((node[0], node[1] - 1))
        if node[1] < len(matrix[0]) - 1 and -1 <= matrix[node[0]][node[1] + 1] - matrix[node[0]][node[1]]:
            neighbors.append((node[0], node[1] + 1))
        return neighbors

    p = PriorityQueue()
    p.put((0, end))
    visited = set()
    while not p.empty():
        counter, (x, y) = p.get()
        if matrix[x][y] == 0:
            return counter
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for neighbor in get_neighbors_inverse((x, y)):
            p.put((counter + 1, neighbor))
    return counter


if __name__ == '__main__':
    input = open("day12.txt", "r").read().splitlines()
    matrix = [[ord(c) - ord("a") for c in line] for line in input]
    start = find_index_2d(matrix, ord("S") - ord("a"))
    end = find_index_2d(matrix, ord("E") - ord("a"))
    matrix[start[0]][start[1]] = 0
    matrix[end[0]][end[1]] = 25
    print(astar(matrix, start, end))
    print(part2(matrix, end))
