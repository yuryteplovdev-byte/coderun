import sys


def main():
    n = int(input())

    word_pairs = []

    for i in range(n):
        word_pair = input().split()
        word_pairs.append(word_pair)

    search_word = input()

    for i in word_pairs:
        if search_word == i[0]:
            print(i[1])
        elif search_word == i[1]:
            print(i[0])



if __name__ == '__main__':
    main()
