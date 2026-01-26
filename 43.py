import sys

def generate_next_step(x, y, dx, dy):
    if x + dx >= 0 and x + dx <= 7 and y + dy >= 0 and y + dy <= 7:
        return (x + dx, y + dy)

    return None

def generate_next_steps(x, y):
    d_steps = [
        (1, 2),
        (-1, 2),
        (1, -2),
        (-1, -2),
        (2, 1),
        (-2, 1),
        (2, -1),
        (-2, -1),
        ]

    result_steps = []

    for i in d_steps:
        next_step = generate_next_step(x, y, i[0], i[1])

        if next_step != None:
            result_steps.append(next_step)
    
    return result_steps


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    horses_coordinat_line = input()

    horse1, horse2 = horses_coordinat_line.split()

    chess_map = {}

    coordinate_x_characters = 'abcdefgh'

    horse1_x = coordinate_x_characters.find(horse1[0])
    horse1_y = int(horse1[1]) - 1

    horse2_x = coordinate_x_characters.find(horse2[0])
    horse2_y = int(horse2[1]) - 1

    steps_queue_of_horse1 = [(horse1_x, horse1_y)]
    steps_queue_of_horse2 = [(horse2_x, horse2_y)]

    steps_count = 0

    while True:

        next_iteration_steps_horse1 = set()
        next_iteration_steps_horse2 = set()

        for i in steps_queue_of_horse1:
            for j in steps_queue_of_horse2:

                if i[0] == j[0] and i[1] == j[1]:
                    print(steps_count)
                    return
                next_iteration_steps_horse2 = set([*next_iteration_steps_horse2, *generate_next_steps(j[0], j[1])])

            next_iteration_steps_horse1 = set([*next_iteration_steps_horse1, *generate_next_steps(i[0], i[1])])

        steps_queue_of_horse1 = next_iteration_steps_horse1
        steps_queue_of_horse2 = next_iteration_steps_horse2

        steps_count += 1
        if steps_count > 4:
            print(-1)
            return 


if __name__ == '__main__':
    main()
