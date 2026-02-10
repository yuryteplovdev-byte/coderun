import sys

def get_min_except_out_of_index(matrix, x, y):
    if y == 0 and x == 0:
        return 0
    elif y == 0:
        return matrix[x-1][y]
    elif x == 0:
        return matrix[x][y-1]
    else:
        return min(matrix[x][y-1], matrix[x-1][y])

def main():
    n, m = map(int, input().split())

    matrix = []

    for _ in range(n):
        row = [int(item) for item in input().split()]

        matrix.append(row)

    result_matrix = []

    for _ in range(n):
        row = []
        for _ in range(m):
            column = None
            row.append(column)
        result_matrix.append(row)

    steps = [
        (0,0)
    ]

    while len(steps) != 0:
        step = steps.pop(0)

        if (result_matrix[step[0]][step[1]]):
            continue

        result_matrix[step[0]][step[1]] = matrix[step[0]][step[1]] + get_min_except_out_of_index(result_matrix, step[0], step[1])

        if step[0] < n-1:
            next_step = (step[0] + 1, step[1])
            steps.append(next_step)
        if step[1] < m-1:
            next_step = (step[0], step[1] + 1)
            steps.append(next_step)

    print(result_matrix[n-1][m-1])

if __name__ == '__main__':
    main()
