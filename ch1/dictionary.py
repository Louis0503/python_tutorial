prices = {
    "ACME" : 45.23,
    "AAPL" : 612.78,
    "IBM" : 205.55,
    "HPQ" : 37.20,
    "FB" : 10.75,
}

def test_min_max_in_dics():
    min_price = min(zip(prices.values(), prices.keys()))
    # zip() will build an once consumed iterator.
    max_price = max(zip(prices.values(), prices.keys()))
    prices_sorted = sorted(zip(prices.values(), prices.keys()))

    print('minimum and maximum in prices wrapped with zip.')
    print(f'{min_price=}\n{max_price=}\n{prices_sorted=}\n')
    print('='*30)

    min_ele = min(prices)
    min_values = min(prices.values())
    print('minimum and maximum in prices dictionary.')
    print(f'{min_ele=}\n{min_values=}\n')
    print('='*30)

    min_price = min(prices, key= lambda k: prices[k])
    print('minimum and maximum in prices.')
    print(f'{min_price=}\n')
    print('='*30)

a = {'x': 1, 'y': 2, 'z': 3}
b = {'x': 11, 'y': 2, 'w': 10}
def find_commons_between_two_dics():
    duplcate_keys = a.keys() & b.keys()
    diff_keys = a.keys() - b.keys()
    print(f'{duplcate_keys=}\n{diff_keys=}\n')

    duplcate_items = a.items() & b.items()
    diff_items = a.items() - b.items()
    print(f'{duplcate_items=}\n{diff_items=}\n')

def my_deque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
        

def remove_duplicate_values_hashable():
    a_1 = [i for i in range(10)]
    a_2 = [i * 2 for i in range(10)]
    a = a_1 + a_2
    print(f'{a_1=}')
    print(f'{a_2=}')
    print(f'{a=}')
    print(f'{list(my_deque(a))=}')
    pass

def unhashable_deque(dicts, key=None):
    seen = set()
    for dic in dicts:
        val = dic if key is None else key(dic)
        if val not in seen:
            yield dic
            seen.add(val)
    pass

def remove_duplicate_values_unhashable():
    a = [
        {'x': 1, 'y': 2 },
        {'x': 1, 'y': 3 },
         {'x': 1, 'y': 2 },
        {'x': 2, 'y': 4 }
    ]
    results = list(unhashable_deque(a, lambda d: (d['x'],d['y'])))
    print(f'{results=}')
    pass

if __name__ == '__main__':
    remove_duplicate_values_unhashable()

