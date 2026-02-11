import sys


def main():
    n, m = map(int, input().split())

    matrix = []

    for _ in range(n):
        row = [int(item) for item in input().split()]
        matrix.append(row)

    result = ResultMatrix(n, m)

    result.set_field(matrix)

    result_cell = result.calculate()
    print(result_cell.value)
    print(' '.join(result_cell.path))

class Cell:
    value = 0
    path = []

class ResultMatrix:

    n = None
    m = None

    field = []

    result_matrix = []
    def __init__(self, n, m):
        self.generate_empty_result_matrix(n, m)
        self.n = n
        self.m = m

    def generate_empty_result_matrix(self, n, m):
        for _ in range(n):
            row = []
            for _ in range(m):
                column = None
                row.append(column)
            self.result_matrix.append(row)

    def set_field(self, field):
        self.field = field

    current_layer = 0

    def calculate(self):

        layer_coordinates = self.get_next_layer_coordinates()

        while len(layer_coordinates) != 0:

            for i in layer_coordinates:
                x = i[0]
                y = i[1]
                self.result_matrix[x][y] = self.calculate_cell(x, y)

            layer_coordinates = self.get_next_layer_coordinates()
            
        return self.result_matrix[self.n-1][self.m-1]

    def get_next_layer_coordinates(self):
        layer_coordinates = []

        for i in range(self.current_layer+1):
            x = i
            y = self.current_layer - i
            if x >= 0 and x < self.n and y >= 0 and y < self.m:
                layer_coordinates.append((x, y))

        self.current_layer += 1

        return layer_coordinates


    def calculate_cell(self, x, y):
        cell_value = self.field[x][y]
        cell = Cell()
        if x == 0 and y == 0:
            cell.value = cell_value
            cell.path = []
        elif x == 0:
            cell.value = cell_value + self.result_matrix[x][y-1].value
            cell.path = self.result_matrix[x][y-1].path + ['R']
        elif y == 0:
            cell.value = cell_value + self.result_matrix[x-1][y].value
            cell.path = self.result_matrix[x-1][y].path + ['D']
        else:
            if (self.result_matrix[x-1][y].value >= self.result_matrix[x][y-1].value):
                cell.value = cell_value + self.result_matrix[x-1][y].value
                cell.path = self.result_matrix[x-1][y].path + ['D']
            else:
                cell.value = cell_value + self.result_matrix[x][y-1].value
                cell.path = self.result_matrix[x][y-1].path + ['R']

        return cell


if __name__ == '__main__':
    main()