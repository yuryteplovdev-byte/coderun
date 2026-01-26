import sys

def move_first_to_last(s):
    if not s:  # Handle empty strings
        return s
    first_char = s[0]
    remaining_chars = s[1:]
    return remaining_chars + first_char

def move_last_to_first(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[:-1]

def generate_next_steps(number):
    next_number_list = []

    if int(number[-1]) > 1:
        current_number = number
        new_digit = str(int(current_number[-1]) - 1)
        current_number = current_number[:-1] + new_digit
        next_number_list.append(current_number)

    if int(number[0]) < 9:
        current_number = number
        new_digit = str(int(current_number[0]) + 1)
        current_number = new_digit + current_number[1:]
        next_number_list.append(current_number)

    next_number_list.append(move_first_to_last(number))
    next_number_list.append(move_last_to_first(number))

    return next_number_list


def main():

    a = input()
    b = input()

    step_queue = [[a]]

    visited_numbers = [a]

    while len(step_queue) != 0:
        current_step = step_queue.pop(0)

        current_number = current_step[-1]

        next_number_list = generate_next_steps(current_number)

        for i in next_number_list:

            if i == b:
                for i in current_step:
                    print(i)
                print(b)
                return

            if i not in visited_numbers:
                visited_numbers.append(i)
                step_queue.append([*current_step, i])


if __name__ == '__main__':
    main()
