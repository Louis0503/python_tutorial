import random
import time

res = random.sample(range(-10000, 10000), 20000)

def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        if 'log_time' in kwargs:
            name = kwargs.get('log_name', method.__name__.upper())
            kwargs['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.22f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

def is_greated_than_zero(ele):
    try:
        tmp = int(ele)
        return ele > 0
    except ValueError:
        return False
@timeit
def arr_expression():
    arr = [n for n in res if n > 0]

@timeit
def arr_filer():
    pos = (n for n in res if n > 0)
    arr = [x for x in pos]

@timeit
def list_lambda_filter():
    arr = list(filter(lambda x: x > 0, res))
    
@timeit
def list_func_filter():
    arr = [x for x in filter(is_greated_than_zero, res)]
    #print([x for x in filter(is_greated_than_zero, res)])

def filer_example():
    arr_expression()
    arr_filer()
    list_lambda_filter()
    list_func_filter()
    
    

if __name__ == '__main__':
    filer_example()