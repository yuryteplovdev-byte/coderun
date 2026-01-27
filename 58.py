import sys

def main():
    button_list = input().split()

    number = input()

    button_to_add_counter = 0

    for i in number:
        if i not in button_list:
            button_list.append(i)
            button_to_add_counter += 1

    print(button_to_add_counter)


if __name__ == '__main__':
    main()