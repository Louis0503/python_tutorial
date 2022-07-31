from calendar import prcal
from collections import deque

from collections import deque

lines = [f'test_{i} python\n' for i in range(10)]

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    for line, prev_lines in search(lines, 'python', 5):
        for pline in prev_lines:
            print(pline, end='')
        print(line[:-1], '123',end='\n')
        print('-'*20)

