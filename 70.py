import sys

def main():
    n = int(input())
    items = [int(i) for i in input().split()]
    number = int(input())

    closest_number = items[0]
    closest_change = abs(items[0] - number)

    for i in range(1, n):
        change = abs(items[i] - number)
        if change < closest_change:
            closest_number = items[i]
            closest_change = change

    print(closest_number)

if __name__ == '__main__':
    main()
