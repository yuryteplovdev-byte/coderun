import sys

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    n = int(input())

    relate_matrix = []

    for i in range(n):
        row = [int(value) for value in input().split()]
        relate_matrix.append(row)

    first_point, second_point = map(int, input().split(' '))

    if first_point == second_point:
        print(0)
        return

    first_point -= 1
    second_point -= 1

    point_queue = []

    point_queue.append(first_point)

    distances = [-1 for i in relate_matrix]

    distances[first_point] = 0

    while len(point_queue) != 0:
        current_point = point_queue.pop(0)

        i = relate_matrix[current_point]

        for j in range(len(i)):
            if j == second_point and i[j] == 1:
                print(distances[current_point] + 1)
                return
            elif i[j] == 1:
                if distances[j] == -1:
                    distances[j] = distances[current_point] + 1
                    point_queue.append(j)

    print(-1)


if __name__ == '__main__':
    main()
