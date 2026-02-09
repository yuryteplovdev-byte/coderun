import sys

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    if (a <= d and b <= e) or (a <= e and b <= d):
        print("YES")
        return

    if (a <= d and c <= e) or (a <= e and c <= d):
        print("YES")
        return

    if (b <= d and c <= e) or (b <= e and c <= d):
        print("YES")
        return

    print("NO")

if __name__ == '__main__':
    main()