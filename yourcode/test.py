

if __name__ == '__main__':
    s = [str]
    for i in range(0, 10):
        s.append(str(i))
    s2 = s[0:5]
    s3 = s2[0:4]
    s4 = s3[0:3]
    s6 = s4
    s6.append('3')
    ss = ''
    ls6 = len(s6)
    for i in range(0, ls6):
        ix = s6[i]
        ss = ss + ix
    # print(s2, '= 0123')
