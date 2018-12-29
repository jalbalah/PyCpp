

if __name__ == '__main__':
    # indexing a string
    s = '0123456'
    print(s[1])
    print(s[2])
    print(s[3])
    print('Begin!', '\n')

    # length of string
    i = len(s)
    print('length of', s, 'is', i)

    # substring
    s2 = s[1:i]
    print('s2 is', s2)

    # length of list of strings
    a = [str]
    a.append('0')
    a.append('1')
    a.append('2')
    a.append('3')
    a.append('4')
    i2 = len(a)

    # indexing list of strings
    a2 = a[3:i2]
    print(a2[0])

    # find in string
    s3 = '23'
    i3 = s.find(s3)
    print('position of 23:', i3)

    # find in list of strings
    s4 = '3'
    i4 = a.find(s4)
    print('position of 3:', i4)

