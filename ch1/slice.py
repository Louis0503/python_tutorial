

def naming_slices():
    record = '.'*20 + '100' + '.'*20 + '12.12'
    cost = int(record[20:23]) * float(record[43:48])
    print(f'{cost=}')

    SHARES= slice(20,23)
    PRICE= slice(43,48)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(f'{cost=}')

def attribures_of_slice():
    a = slice(5, 1000, 2)
    print(f'{a=}')
    s = 'HelloWorld'
    a.indices(len(s))
    for i in range(*a.indices(len(s))):
        print(s[i])

if __name__ == '__main__':
    attribures_of_slice()
    pass