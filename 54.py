import sys

def main():
    n = int(input())

    language_count = {}

    for i in range(n):
        m = int(input())
        for j in range(m):
            language = input()
            if language_count.get(language, False):
                language_count[language] += 1
            else:
                language_count[language] = 1


    filtered_dict_keys = {key: value for key, value in language_count.items() if value == n}

    print(len(filtered_dict_keys))
    for key, value in filtered_dict_keys.items():
        print(key)

    print(len(language_count))
    for key, value in language_count.items():
        print(key)




if __name__ == '__main__':
    main()
