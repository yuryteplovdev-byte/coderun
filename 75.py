import sys

def main():
    a = int(input())

    b = int(input())

    n = int(input())

    m = int(input())

    min1 = n + a * (n - 1)
    max1 = n + a * (n + 1)

    min2 = m + b * (m - 1)
    max2 = m + b * (m + 1)

    result_min = max(min1, min2)
    result_max = min(max1, max2)

    if result_min > result_max :
        print(-1)
    else:
        print(result_min, result_max)


if __name__ == '__main__':
    main()
