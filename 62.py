import sys

class UniqueCounter:
    counted_items = {}
    count = 0

    def add(self, item):
        if self.counted_items.get(item) != True:
            self.counted_items[item] = True
            self.count += 1


def main():
    number_group = [int(item) for item in input().split()]

    count = UniqueCounter()

    for i in number_group:
        count.add(i)
    
    print(count.count)


if __name__ == '__main__':
    main()