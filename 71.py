import sys
from enum import Enum

class group_types(Enum):
    CONSTANT = 'CONSTANT'
    ASCENDING = 'ASCENDING'
    WEAKLY_ASCENDING = 'WEAKLY ASCENDING'
    DESCENDING = 'DESCENDING'
    WEAKLY_DESCENDING = 'WEAKLY DESCENDING'
    RANDOM = 'RANDOM'

def main():
    prev_number = None
    group_type = None 

    while True:
        try:
            line = input().strip()
            if not line or line == '-2000000000':
                break
            current_number = int(line)
        except EOFError:
            break

        if prev_number is None:
            prev_number = current_number
            continue

        if group_type == group_types.RANDOM:
            continue

        if group_type is None:
            if current_number > prev_number:
                group_type = group_types.ASCENDING
            elif current_number < prev_number:
                group_type = group_types.DESCENDING
            elif current_number == prev_number:
                group_type = group_types.CONSTANT

        if group_type == group_types.CONSTANT:
            if current_number > prev_number:
                group_type = group_types.WEAKLY_ASCENDING
            elif current_number < prev_number:
                group_type = group_types.WEAKLY_DESCENDING
        
        elif group_type == group_types.ASCENDING:
            if current_number == prev_number:
                group_type = group_types.WEAKLY_ASCENDING
            elif current_number < prev_number:
                group_type = group_types.RANDOM
        
        elif group_type == group_types.DESCENDING:
            if current_number == prev_number:
                group_type = group_types.WEAKLY_DESCENDING
            elif current_number > prev_number:
                group_type = group_types.RANDOM
        
        elif group_type == group_types.WEAKLY_ASCENDING:
            if current_number < prev_number:
                group_type = group_types.RANDOM
        
        elif group_type == group_types.WEAKLY_DESCENDING:
            if current_number > prev_number:
                group_type = group_types.RANDOM

        prev_number = current_number

    if not group_type:
        print(group_types.CONSTANT.value)
    else:
        print(group_type.value)

if __name__ == '__main__':
    main()