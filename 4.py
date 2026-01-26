def recursive_do_step(x, y, target_x, target_y, memo):
    if x == target_x and y == target_y:
        return 1
    if x > target_x or y > target_y:
        return 0

    if (x, y) in memo:
        return memo[(x, y)]

    memo[(x, y)] = (
        recursive_do_step(x + 1, y + 2, target_x, target_y, memo) +
        recursive_do_step(x + 2, y + 1, target_x, target_y, memo)
    )
    return memo[(x, y)]


def main():
    n, m = map(int, input().split(' '))
    print(recursive_do_step(1, 1, n, m, {}))

if __name__ == '__main__':
    main()
