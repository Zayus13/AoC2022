def find_visible_trees(matrix):
    vis = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    counter = 2 * (len(matrix) + len(matrix[0])) - 4
    for i in range(1, len(matrix) - 1):
        maxHeightLeft = matrix[i][0]
        maxHeightRight = matrix[i][-1]
        for j in range(1, len(matrix[0]) - 1):
            if (matrix[i][j] > maxHeightLeft):
                if not vis[i][j]:
                    counter += 1
                maxHeightLeft = matrix[i][j]
                vis[i][j] = True

            if (matrix[i][len(matrix[0]) - 1 - j] > maxHeightRight):
                if not vis[i][len(matrix[0]) - 1 - j]:
                    counter += 1
                maxHeightRight = matrix[i][len(matrix[0]) - 1 - j]
                vis[i][len(matrix[0]) - 1 - j] = True

    for i in range(1, len(matrix[0]) - 1):
        maxHeightUp = matrix[0][i]
        maxHeightDown = matrix[-1][i]
        for j in range(1, len(matrix) - 1):
            if (matrix[j][i] > maxHeightUp):
                if not vis[j][i]:
                    counter += 1
                maxHeightUp = matrix[j][i]
                vis[j][i] = True

            if (matrix[len(matrix) - 1 - j][i] > maxHeightDown):
                if not vis[len(matrix) - 1 - j][i]:
                    counter += 1
                maxHeightDown = matrix[len(matrix) - 1 - j][i]
                vis[len(matrix) - 1 - j][i] = True
    return counter


def calculate_view_distance(matrix):
    vis = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            scores = [0, 0, 0, 0]
            for left in range(1, j + 1):
                scores[0] += 1
                if matrix[i][j - left] >= matrix[i][j]:
                    break

            for right in range(1, len(matrix[0]) - j):
                scores[1] += 1
                if matrix[i][j + right] >= matrix[i][j]:
                    break

            for up in range(1, i + 1):
                scores[2] += 1
                if matrix[i - up][j] >= matrix[i][j]:
                    break
            for down in range(1, len(matrix) - i):
                scores[3] += 1
                if matrix[i + down][j] >= matrix[i][j]:
                    break
            vis[i][j] = scores[0] * scores[1] * scores[2] * scores[3]
    return max([max(row) for row in vis])


if __name__ == '__main__':
    f = open("day08.txt", "r")
    lines = f.read().splitlines()
    matrix = [list(map(int, line)) for line in lines]
    print(find_visible_trees(matrix))
    print(calculate_view_distance(matrix))
