from collections import Counter

s1 = 'look into my eyes '*2 \
     + 'the eyes '*3 \
     + "don't look around the eyes you're under"
s2 = 'look into my eyes '*8 \
     + 'why are you not looing into my eyes'

def test_counter():
    s1 =  s1.split(' ')
    s2 =  s2.split(' ')
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    print(f'{s1_counter.most_common(3)=}')
    print(f"{s1_counter['eyes']=}")
    print(f"{s2_counter['eyes']=}")
    print(f'{(s1_counter - s2_counter)=}')

if __name__ == '__main__':
    print('HelloWorld')
    pass