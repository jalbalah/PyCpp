

if __name__ == '__main__':
    # indexing a string
    s = '0123456'
    print(s[1])
    print(s[2])
    print(s[3])
    print('Begin!', '\n')

    # length of string
    i = len(s)
    s2 = s[1:i]
    print('length:', s2)

    # length of list of strings
    a = [str]
    a.append('0')
    a.append('1')
    a.append('2')
    a.append('3')
    a.append('4')
    i2 = len(a)

    # indexing list of strings
    #a2 = a[3:i2]
    #print(a2[0])

    #a3 = [float]
    #a3.append(0)
    #a3.append(1)
    #a3.append(2)
    #a3.append(3)
    #a4 = a3[0:1]
    #i3 = len(a4)
    #print(a4[i3])
