import sys

def main():
    first_line_length = int(input())
    first_line = [int(item) for item in input().split()]

    second_line_length = int(input())
    second_line = [int(item) for item in input().split()]

    print(first_line_length)
    print(first_line)

    print(second_line_length)
    print(second_line)

    #TODO

if __name__ == '__main__':
    main()