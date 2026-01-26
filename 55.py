import sys

def main():
    n = int(input())

    birds_coordinates = []

    for i in range(n):
        line = input().split()

        birds_coordinates.append((int(line[0]), int(line[1])))


    sorted_birds_coordinates = sorted(
        birds_coordinates, 
        key=lambda i: (i[1], i[0])
        )

    shot_counter = 0

    while len(sorted_birds_coordinates) != 0:
        shot_counter += 1
        current_item = sorted_birds_coordinates[0]
        alive_birds_coords = list(
            filter(
                lambda i: i[0] != current_item[0],
                sorted_birds_coordinates
                )
            )
        sorted_birds_coordinates = alive_birds_coords

    print(shot_counter)

if __name__ == '__main__':
    main()