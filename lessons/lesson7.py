

if __name__ == '__main__':
    s = 'xoxoxo\nhello world'

    fw = open('tests/test.txt', 'w')
    fw.write(s)

    fr = open('tests/test.txt', 'r').readlines()
    print(fr[0] + " " + fr[1])

    for line in fr:
        print(line)
