import sys

def main():

    text = ''

    for line_string in sys.stdin:
        line_string = line_string.strip()
        
        if not line_string:
            continue
            
        text += line_string + ' '

    words = text.split()

    words_count = {}

    for i in words:
        if words_count.get(i, None) == None:
            words_count[i] = 0
        else: 
            words_count[i] += 1

        print(words_count[i], end=' ')



if __name__ == '__main__':
    main()
