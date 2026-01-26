import sys

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    matrix = []
    

    for line_string in sys.stdin:
        line_string = line_string.strip()
        
        if not line_string:
            continue
            
        line = line_string.split()
        
        first_point = int(line[0])
        second_point = int(line[1])
        
        matrix.append((first_point, second_point))



    visited_points = []
    points_to_visit = [1]

    while len(points_to_visit) != 0:
        current_point = points_to_visit.pop()
        relations_to_current_point = filter(lambda x: x[1] == current_point, matrix)

        visited_points.append(current_point)
        
        for i in relations_to_current_point:
            if i[0] not in visited_points and i[0] not in points_to_visit:
                points_to_visit.append(i[0])

    visited_points.sort()
        
    print(' '.join(str(i) for i in visited_points))

if __name__ == '__main__':
    main()