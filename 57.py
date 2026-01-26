import sys

def main():
    first_gen = input()
    second_gen = input()

    pair_counter = 0

    second_gen_pairs = {}

    for i in range(len(second_gen)-1):
        second_gen_pairs[second_gen[i] + second_gen[i+1]] = True

    for i in range(len(first_gen)-1):
        if second_gen_pairs.get(first_gen[i] + first_gen[i+1]) == True:
            pair_counter += 1

    print(pair_counter)

if __name__ == '__main__':
    main()