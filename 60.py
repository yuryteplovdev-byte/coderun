import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    anya_set = set(map(int, input_data[2 : 2 + n]))
    borya_set = set(map(int, input_data[2 + n : 2 + n + m]))

    same = sorted(anya_set.intersection(borya_set))
    
    only_anya = sorted(anya_set.difference(borya_set))
    
    only_borya = sorted(borya_set.difference(anya_set))

    sys.stdout.write(f"{len(same)}\n{' '.join(map(str, same))}\n")
    sys.stdout.write(f"{len(only_anya)}\n{' '.join(map(str, only_anya))}\n")
    sys.stdout.write(f"{len(only_borya)}\n{' '.join(map(str, only_borya))}\n")

if __name__ == '__main__':
    main()
