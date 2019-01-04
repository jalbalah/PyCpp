

if __name__ == '__main__':
    s = '0123456'
    s2 = s[0:5]
    s3 = s2[0:4]
    s4 = s3[0:3]
    s5 = '3'
    s6 = s4 + s5
    print(s6, '= 0123')

    s7 = [str]
    for i in range(0, 10000000):
        s7.append(str(i))
    s8 = ','.join(s7)
    print('writing file')
    f = open('yourcode/test.txt', 'w')
    f.write(s8)
