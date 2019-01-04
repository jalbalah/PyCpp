

if __name__ == '__main__':
    #s = '0123456'
    #s2 = s[0:5]
    #s3 = s2[0:4]
    #s4 = s3[0:3]
    #s5 = '3'
    #s6 = s4 + s5
    #print(s6, '= 0123')

    s7 = ''
    for i in range(0, 100):
        s8 = str(i)
        s7 = s7 + ', (' + s8 + ')'
    l7 = len(s7)
    s9 = s7[2:l7]
    print(s9)
