import sys

class Field:

    field = []

    m = 0
    n = 0

    def __init__(self, n, m):
        self.m = m
        self.n = n
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            self.field.append(row)

    def print(self):
        for i in self.field:
            print(' '.join([str(j) for j in i]))

    def put_mine(self, x, y):
        self.field[x][y] = '*'
        steps = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
            (x+1, y+1),
            (x-1, y+1),
            (x+1, y-1),
            (x-1, y-1),
        ]

        for i in steps:
            if i[0]>=0 and i[0]<self.n and i[1]>=0 and i[1]<self.m:
                if self.field[i[0]][i[1]] != '*':
                    self.field[i[0]][i[1]] += 1
            

def main():

    line = input().split()

    n, m, k = int(line[0]), int(line[1]), int(line[2])

    field = Field(n, m)

    for i in range(k):
        line = input().split()
        field.put_mine(int(line[0])-1, int(line[1])-1) 

    field.print()


if __name__ == '__main__':
    main()