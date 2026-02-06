import sys

def main():
    numbers = [int(item) for item in input().split()]

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i-1]:
            print("NO")
            return

    print("YES")
    return


if __name__ == '__main__':
    main()
