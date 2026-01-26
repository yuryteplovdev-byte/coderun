import sys

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    n = int(input())

    under_lists = []

    data_array = [int(i) for i in input().split()]

    for i in data_array:
        current_underlist = [i]
        if (len(under_lists) != 0):
            for j in under_lists:
                if len(current_underlist) <= len(j) and j[-1] < i:
                    current_underlist = j.copy()
                    current_underlist.append(i)

        under_lists.append(current_underlist)

    max_len_underlist = []

    for i in under_lists:
        if len(i) > len(max_len_underlist):
            max_len_underlist = i

    print(' '.join(str(i) for i in max_len_underlist))


if __name__ == '__main__':
    main()
