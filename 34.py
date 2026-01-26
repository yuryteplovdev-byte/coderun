import sys

cache = {}


def calculate_route(direction, param, rules):
    if param == 1:
        return 1
    else:
        if (direction, param) in cache:
            return cache[(direction, param)]
        result = 1
        for i in rules[direction]:
            result += calculate_route(i, param-1, rules)

        cache[(direction, param)] = result
        return result

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    directions = 'NSWEUD'

    direction_rules = {}

    for i in directions:
        direction_rules[i] = input()

    first_step = input().split()

    first_step_direction = first_step[0]
    first_step_param = int(first_step[1])

    print(calculate_route(first_step_direction, first_step_param, direction_rules))


if __name__ == '__main__':
    main()
