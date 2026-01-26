
import sys

def is_point_in_range(x, y, n, m, matrix):
    return x >= 0 and x < n and y >= 0 and y < m and matrix[x][y] == -1

def main():

    n, m, s, t, q = map(int, input().split(' '))

    coordinates = []

    for i in range(q):
        x, y = map(int, input().split(' '))
        coordinates.append((x, y))

    matrix = []

    for x in range(n):
        matrix.append([-1 for i in range(m)])

    matrix[s-1][t-1] = 0

    step_queue = []
    step_queue.append((s-1, t-1))

    while len(step_queue) != 0:
        current_point = step_queue.pop(0)

        print(current_point)

        if is_point_in_range(current_point[0]+2, current_point[1]+1, n, m, matrix):
            matrix[current_point[0]+2][ current_point[1]+1] = matrix[current_point[0]][current_point[1]] + 1
            step_queue.append((current_point[0]+2, current_point[1]+1))

        if is_point_in_range(current_point[0]+1, current_point[1]+2, n, m, matrix):
            matrix[current_point[0]+1][ current_point[1]+2] = matrix[current_point[0]][current_point[1]] + 1
            step_queue.append((current_point[0]+1, current_point[1]+2))

        if is_point_in_range(current_point[0]-2, current_point[1]-1, n, m, matrix):
            matrix[current_point[0]-2][ current_point[1]-1] = matrix[current_point[0]][current_point[1]] + 1
            step_queue.append((current_point[0]-2, current_point[1]-1))

        if is_point_in_range(current_point[0]-1, current_point[1]-2, n, m, matrix):
            matrix[current_point[0]-1][ current_point[1]-2] = matrix[current_point[0]][current_point[1]] + 1
            step_queue.append((current_point[0]-1, current_point[1]-2))

        if is_point_in_range(current_point[0]-2, current_point[1]+1, n, m, matrix):
            matrix[current_point[0]-2][ current_point[1]+1] = matrix[current_point[0]][current_point[1]] + 1
            step_queue.append((current_point[0]-2, current_point[1]+1))

        if is_point_in_range(current_point[0]-1, current_point[1]+2, n, m, matrix):
            matrix[current_point[0]-1][ current_point[1]+2] = matrix[current_point[0]][current_point[1]] + 1
            step_queue.append((current_point[0]-1, current_point[1]+2))

        if is_point_in_range(current_point[0]+2, current_point[1]-1, n, m, matrix):
            matrix[current_point[0]+2][ current_point[1]-1] = matrix[current_point[0]][current_point[1]] + 1
            step_queue.append((current_point[0]+2, current_point[1]-1))

        if is_point_in_range(current_point[0]+1, current_point[1]-2, n, m, matrix):
            matrix[current_point[0]+1][ current_point[1]-2] = matrix[current_point[0]][current_point[1]] + 1
            step_queue.append((current_point[0]+1, current_point[1]-2))

    sum = 0

    for i in coordinates:
        if matrix[i[0]-1][i[1]-1] == -1:
            print(-1)
            return
        sum += matrix[i[0]-1][i[1]-1]
    print(sum)
    return 




if __name__ == '__main__':
    main()
