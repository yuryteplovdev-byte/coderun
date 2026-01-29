import sys

class SortedGroup:
    group = []
    def insert_item(self, item):
        for key, value in enumerate(self.group):
            if (value > item) :
                self.group.insert(key, item)
                return
        self.group.append(item)
    def __str__(self):
        return " ".join([str(item) for item in self.group])
        

def main():

    sorted_merged_group = SortedGroup()

    first_group = [int(item) for item in input().split()]
    second_group = [int(item) for item in input().split()]

    second_group_to_find = {}

    for i in second_group:
        second_group_to_find[i] = True

    for i in first_group:
        if second_group_to_find.get(i) == True:
            sorted_merged_group.insert_item(i)

    print(sorted_merged_group)


if __name__ == '__main__':
    main()
