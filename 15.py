import sys

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    n = int(input())

    matrix = []
    steps = []

    start = (0,0,0)

    for i in range(n):
        input()
        matrix_2d = []
        steps_2d = []
        for j in range(n):
            line = input()
            steps_line = [-1 for i in line]
            x_start_point = line.find('S')
            if x_start_point != -1:
                start = [i, j, x_start_point]
                steps_line[x_start_point] = 0

            matrix_2d.append(line)
            steps_2d.append(steps_line)
        matrix.append(matrix_2d)
        steps.append(steps_2d)
            
    queue_step = [start] 

    # print(steps)

    while len(queue_step) != 0:
        cs = queue_step.pop(0)
        # print(cs)

        if cs[0] == 0:
            print(steps[cs[0]][cs[1]][cs[2]])
            return

        if cs[0] < n-1 and (matrix[cs[0]+1][cs[1]][cs[2]] == '.') and steps[cs[0]+1][cs[1]][cs[2]] == -1:
            steps[cs[0]+1][cs[1]][cs[2]] = steps[cs[0]][cs[1]][cs[2]] + 1
            queue_step.append((cs[0]+1, cs[1], cs[2]))

        if cs[0] > 0 and (matrix[cs[0]-1][cs[1]][cs[2]] == '.') and steps[cs[0]-1][cs[1]][cs[2]] == -1:
            steps[cs[0]-1][cs[1]][cs[2]] = steps[cs[0]][cs[1]][cs[2]] + 1
            queue_step.append((cs[0]-1, cs[1], cs[2]))

        if cs[1] < n-1 and (matrix[cs[0]][cs[1] + 1][cs[2]] == '.') and steps[cs[0]][cs[1]+1][cs[2]] == -1:
            steps[cs[0]][cs[1] + 1][cs[2]] = steps[cs[0]][cs[1]][cs[2]] + 1
            queue_step.append((cs[0], cs[1] + 1, cs[2]))

        if cs[1] > 0 and (matrix[cs[0]][cs[1] - 1][cs[2]] == '.') and steps[cs[0]][cs[1]-1][cs[2]] == -1:
            steps[cs[0]][cs[1] - 1][cs[2]] = steps[cs[0]][cs[1]][cs[2]] + 1
            queue_step.append((cs[0], cs[1] - 1, cs[2]))

        if cs[2] < n-1 and (matrix[cs[0]][cs[1]][cs[2] + 1] == '.') and steps[cs[0]][cs[1]][cs[2]+1] == -1:
            steps[cs[0]][cs[1]][cs[2] + 1] = steps[cs[0]][cs[1]][cs[2]] + 1
            queue_step.append((cs[0], cs[1], cs[2] + 1))

        if cs[2] > 0 and (matrix[cs[0]][cs[1]][cs[2] - 1] == '.') and steps[cs[0]][cs[1]][cs[2]-1] == -1:
            steps[cs[0]][cs[1]][cs[2] - 1] = steps[cs[0]][cs[1]][cs[2]] + 1
            queue_step.append((cs[0], cs[1], cs[2] - 1))

    print(-1)



if __name__ == '__main__':
    main()
