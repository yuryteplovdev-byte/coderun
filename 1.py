import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    a, b, c = map(int, input().split())

    if (a >= b and b >= c) or (c >= b and b >= a):
        print(b)

    elif (a >= c and c >= b) or (b >= c and c >= a):
        print(c)

    else:
        print(a)

    pass


if __name__ == '__main__':
    main()
